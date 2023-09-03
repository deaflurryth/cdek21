import ipaddress

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app.database import engine
from app.endpoints.cdek_calc.rout import calculator_cdek
from app.endpoints.email_form.router import router
from app.endpoints.email_form.models import Email_form
from sqladmin import ModelView, Admin
from fastapi.responses import Response, RedirectResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


async def not_found_error(request: Request, exc: HTTPException):
    return templates.TemplateResponse("templates/404.html", {"request": request})


exception_handlers = {404: not_found_error}

app = FastAPI(
    title="Cdek 21",
    exception_handlers=exception_handlers,
)


@app.exception_handler(HTTPException)
async def not_found_error(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse("templates/404.html", {"request": request})
    raise exc


admin = Admin(app, engine)
app.include_router(router)
app.include_router(calculator_cdek)

templates = Jinja2Templates(directory="app/public/")
app.mount("/", StaticFiles(directory="app/public/", html=True), name="static")


@app.middleware("http")
async def check_admin_access(request: Request, call_next):
    if request.url.path == "/admin/":
        return RedirectResponse(url="/")
    user = request.query_params.get("user")
    password = request.query_params.get("password")
    if user == "cdek21" and password == "cdek21password":
        return RedirectResponse(url="/admin/")

    response = await call_next(request)
    return response


class Email_formAdmin(ModelView, model=Email_form):
    column_list = [Email_form.id, Email_form.name, Email_form.phone, Email_form.description]


admin.add_view(Email_formAdmin)


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
    "https://cdek-cdek21vek.amvera.io/",
    "https://cdek-cdek21vek.amvera.io",
    "https://cdek21vek.ru/",
    "https://cdek21vek.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
