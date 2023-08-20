from fastapi import FastAPI

from server.app.database import engine
from server.app.endpoints.cdek_calc.rout import calculator_cdek
from server.app.endpoints.email_form.router import router
from server.app.endpoints.email_form.models import Email_form
from sqladmin import ModelView, Admin

app = FastAPI(
    title="Cdek 21"
)


class Email_formAdmin(ModelView, model=Email_form):
    column_list = [Email_form.id, Email_form.name, Email_form.phone]


admin = Admin(app, engine)
app.include_router(router)
app.include_router(calculator_cdek)

admin.add_view(Email_formAdmin)