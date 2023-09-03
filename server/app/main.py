import ipaddress

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.endpoints.cdek_calc.rout import calculator_cdek
from app.endpoints.email_form.router import router
from app.endpoints.email_form.models import Email_form
from sqladmin import ModelView, Admin
from fastapi.responses import Response
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


async def not_found_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse("index.html", {"request": request})


exception_handlers = {404: not_found_error}

app = FastAPI(
    title="Cdek 21",
    exception_handlers=exception_handlers,
)
admin = Admin(app, engine)
app.include_router(router)
app.include_router(calculator_cdek)

allowed_users = ["51.158.37.29/32"]

@app.middleware("http")
async def check_admin_access(request: Request, call_next):
    path = request.url.path
    client_ip = request.client.host
    print(client_ip)
    if (path.startswith("/admin/") or path.startswith("/docs")) and not is_ip_in_allowed_list(client_ip):
        return templates.TemplateResponse("404.html", {"request": request})
    response = await call_next(request)
    return response


def is_ip_in_allowed_list(ip):
    for allowed_ip in allowed_users:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(allowed_ip, strict=False):
            return True
    return False


class Email_formAdmin(ModelView, model=Email_form):
    column_list = [Email_form.id, Email_form.name, Email_form.phone, Email_form.description]


admin.add_view(Email_formAdmin)

templates = Jinja2Templates(directory="app/public/")
app.mount("/", StaticFiles(directory="app/public/", html=True), name="static")


@app.get("/")
async def serve_spa(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


origins = [
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://brawl-test.onrender.com",
    "https://a1c8-46-148-105-36.ngrok-free.app",
    "localhost:3000",
    "127.0.0.1:3000",
    "127.0.0.1:8000",
    "https://brawlcase-danyanara.amvera.io",
    "https://brawlcases.com",
    "https://www.brawlcases.com",
    "https://test-cdek-danyanara.amvera.io",
    "https://test-cdek-danyanara.amvera.io/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
