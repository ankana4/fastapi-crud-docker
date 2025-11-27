import aiosmtplib
from email.message import EmailMessage
from app.core.config import settings

async def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["from"] = settings.SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)
    
    await aiosmtplib.send(
        msg,
        hostname=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_USER,
        password=settings.SMTP_PASSWORD,
        start_tls=True
    )