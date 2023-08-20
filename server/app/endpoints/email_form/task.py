import smtplib
from email.message import EmailMessage
from server.app.config import SMTP_PASSWORD, SMTP_USER

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


async def get_email_template_dashboard(email_to: str, name: str, telephone: str):
    email = EmailMessage()
    email['Subject'] = 'CDEK 21'
    email['From'] = SMTP_USER
    email['To'] = email_to

    email.set_content(f"""{name}, Телефон = {telephone} """)
    return email


async def send_email_report_dashboard(email_to: str, name: str, telephone: str):
    email = await get_email_template_dashboard(email_to, name, telephone)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
