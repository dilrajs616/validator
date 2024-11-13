from flask import request, jsonify
from app import app
from random import randint
from checkEmail import email_exists
from sendMail import sendEmail

@app.route('/validate', methods=["GET","POST"])
def validate():
    if request.method == "GET":
        return jsonify({"message" : "response to not throw an error"})
    
    if request.method == "POST":
        email = request.form.get("email")
        if not email_exists(email):
            return jsonify({"code":"error","message": f"invalid email received: {email}"})
        otp = randint(100000,999999)
        sendEmail(email, "OTP for email verification", otp)
    return jsonify({"success": "True", "otp": otp})  