import smtplib
import dns.resolver
import socket

def check_mx_record(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        for mx in mx_records:
            mx_record = str(mx.exchange).rstrip('.')
            # Skip any invalid MX records
            if "invalid" not in mx_record:
                return mx_record
        return None
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return None

def check_smtp_connection(mx_record, email):
    try:
        # Try to connect to the mail server on different SMTP ports
        for port in [25, 587, 465]:
            try:
                # Set up the connection with a specific port
                server = smtplib.SMTP(mx_record, port, timeout=10)
                server.set_debuglevel(1)  # Enable debugging info for visibility
                
                if port == 587:
                    server.starttls()  # Start TLS if using port 587

                server.helo("example.com")  # Dummy domain used in HELO
                server.mail("test@example.com")  # Dummy sender email
                code, message = server.rcpt(str(email))  # RCPT TO command for the recipient email
                server.quit()

                # If the server responds with code 250, email likely exists
                if code == 250:
                    return True
            except smtplib.SMTPConnectError as e:
                print(f"Connection error on port {port}: {e}")
            except smtplib.SMTPServerDisconnected:
                print(f"Server disconnected on port {port}")
            except socket.error as e:
                print(f"Socket error on port {port}: {e}")
        return False
    except (smtplib.SMTPException, socket.error) as e:
        print(f"General SMTP error: {e}")
        return False

def email_exists(email):
    # Split the email to get the domain
    domain = email.split('@')[-1]
    
    # Check MX record for the domain
    mx_record = check_mx_record(domain)
    if not mx_record:
        return False, "No valid MX record for the domain"
    
    # Check SMTP server connection and see if email is accepted
    email_valid = check_smtp_connection(mx_record, email)
    if email_valid:
        return True, "Email address exists"
    else:
        return False, "Email address does not exist or server rejected it"
