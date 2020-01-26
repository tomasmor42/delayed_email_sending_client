import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email_with_text(text, email_from, email_to):
    message = Mail(
        from_email=email_from,
        to_emails=email_to,
        subject='Email from the past',
        html_content=f'<strong>{text}</strong>')
    try:
        sg = SendGridAPIClient(os.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return response
    except Exception as e:
        print(e.message)