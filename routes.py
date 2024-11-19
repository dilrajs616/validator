from flask import request, jsonify
from app import app
from random import randint
from sendMail import sendEmail
import asyncio

async def main(receiver_email, otp):  
    subject = "OTP"
    message = f"OTP for sign up is: {otp}"
    return await sendEmail(receiver_email, subject, message)

@app.route('/validate', methods=["GET","POST"])
def validate():
    if request.method == "GET":
        return jsonify({"message" : "response to not throw an error"})
    
    if request.method == "POST":
        email = request.form.get("email")
        if not email.endswith("@gndec.ac.in"):
            return jsonify({"code":"error","message": f"invalid email received: {email}"})
        otp = randint(100000,999999)
        asyncio.run(main(email, otp))
        return jsonify({"success": "True", "otp": otp})  
