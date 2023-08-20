from fastapi import APIRouter
from sqlalchemy import select
from server.app.endpoints.email_form.models import Email_form

from server.app.endpoints.email_form.task import send_email_report_dashboard
# from app.api.endpoints.tasks.tasks2 import send_email_async
from server.app.database import async_session_maker
from server.app.config import SMTP_TO_USER

router = APIRouter(prefix="/report")


@router.get("/dashboard")
async def get_dashboard_report(name: str, telephone: str):
    await send_email_report_dashboard(SMTP_TO_USER, name, telephone)
    async with async_session_maker() as session:
        email = select(Email_form).where(Email_form.phone == telephone)
        result = await session.execute(email)
        existing_email = result.scalar_one_or_none()
        if existing_email is None:
            new_user = Email_form(name=name, phone=telephone)
            session.add(new_user)
        await session.commit()

    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
