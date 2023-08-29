from fastapi import APIRouter, BackgroundTasks
from sqlalchemy import select
from app.endpoints.email_form.models import Email_form
from pydantic import BaseModel
from app.endpoints.email_form.task import send_email_report_dashboard
# from app.api.endpoints.tasks.tasks2 import send_email_async
from app.database import async_session_maker
from app.config import SMTP_TO_USER
from pydantic.class_validators import Optional

router = APIRouter(prefix="/report")


class FormCall(BaseModel):
    name: str
    phone: str
    descriprion: Optional[str] = None


@router.post("/dashboard")
async def get_dashboard_report(data: FormCall):
    try:
        async with async_session_maker() as session:

            name = data.name
            phone = data.phone
            info = data.descriprion
            if info is None:
                await send_email_report_dashboard(name, phone)
                new_user = Email_form(name=name, phone=phone)
            else:
                await send_email_report_dashboard(name, phone, info)
                new_user = Email_form(name=name, phone=phone, description=info)
            session.add(new_user)

            await session.commit()

        return {
            "status": 200,
            "data": "Письмо отправлено",
            "details": None
        }
    except Exception as e:
        print(e)
