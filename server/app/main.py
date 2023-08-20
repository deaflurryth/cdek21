from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.endpoints.cdek_calc.rout import calculator_cdek
from app.endpoints.email_form.router import router
from app.endpoints.email_form.models import Email_form
# from sqladmin import ModelView, Admin
from fastapi.responses import Response
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Cdek 21"
)




# class Email_formAdmin(ModelView, model=Email_form):
#     column_list = [Email_form.id, Email_form.name, Email_form.phone]


templates = Jinja2Templates(directory="app/public/")
app.mount("/", StaticFiles(directory="app/public/", html=True), name="static")


@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# admin = Admin(app, engine)
app.include_router(router)
app.include_router(calculator_cdek)

# admin.add_view(Email_formAdmin)


origins = [
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://brawl-test.onrender.com",
    "https://a1c8-46-148-105-36.ngrok-free.app",
    "localhost:3000",
    "127.0.0.1:3000",
    "https://brawlcase-danyanara.amvera.io",
    "https://brawlcases.com",
    "https://www.brawlcases.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)