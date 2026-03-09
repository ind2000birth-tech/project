from flask_mail import Message
from app.extensions import mail
from flask import current_app

class EmailService:
    @staticmethod
    def send_contact_email(name, email, message):
        try:
            msg = Message(
                subject=f"New Portfolio Contact from {name}",
                recipients=[current_app.config['MAIL_DEFAULT_SENDER']],
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )
            mail.send(msg)
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
