import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import SMTP_PASSWORD, SMTP_USER, SMTP_TO_USER

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


async def get_email_template_dashboard(name: str, telephone: str, info=None):
    email = MIMEMultipart()
    email['Subject'] = 'CDEK 21'
    email['From'] = SMTP_USER
    email['To'] = SMTP_TO_USER

    html_content = f"""
    <html>
    <head></head>
    <body>
        <table style="border-collapse: collapse; width: 50%;">
            <tr>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">Name</td>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">{name}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">Telephone</td>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">{telephone}</td>
            </tr>
    """

    if info:
        html_content += f"""
            <tr>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">Description</td>
                <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">{info}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    email.attach(MIMEText(html_content, 'html'))

    return email


async def send_email_report_dashboard(name: str, telephone: str, info=None):
    email = await get_email_template_dashboard(name, telephone, info)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
