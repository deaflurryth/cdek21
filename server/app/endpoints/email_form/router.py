from fastapi import APIRouter
from sqlalchemy import select
from app.endpoints.email_form.models import Email_form
from pydantic import BaseModel
from app.endpoints.email_form.task import send_email_report_dashboard
# from app.api.endpoints.tasks.tasks2 import send_email_async
from app.database import async_session_maker
from app.config import SMTP_TO_USER

router = APIRouter(prefix="/report")

class FormCall(BaseModel):
    name: str
    telephone: str

@router.post("/dashboard")
async def get_dashboard_report(data: FormCall):
    try:
        name =  data.name
        telephone = data.telephone
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
    except Exception as e:
        print(e)

