from typing import List
from ..config import Config
from fastapi import BackgroundTasks, FastAPI, APIRouter
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Template

class EmailSchema(BaseModel):
    email: List[EmailStr]

class EmailContent(BaseModel):
    message:str
    subject: str

templates = Jinja2Templates(directory="templates")

conf = ConnectionConfig(
    MAIL_USERNAME = Config.MAIL_USERNAME,
    MAIL_PASSWORD = Config.MAIL_PASSWORD,
    MAIL_FROM = Config.MAIL_FROM,
    MAIL_PORT = 465,
    MAIL_SERVER = Config.MAIL_SERVER,
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

router = APIRouter()


@router.post('/email/testmail/')
async def TestMail(content:EmailContent, recipients:EmailSchema):
    html = Template("""
        <div class="container>
        <br>
        <p> Good day</p>
        <br>
        <p>{content.message}</p>
        <br>
        <p>please verify your account </p>
        <button class="btn btn-success" type="submit> Verify </button>

        """
    )

        
    message = MessageSchema(
    subject=content.subject,
    recipients=recipients.model_dump().get('email'),
    body=html.render(url='https://example.com/confirm'),
    subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@router.post('/email/verification/')
async def VerificationSendEmail(user_email:str, content: EmailContent):

    html = f"""
    <div class="container>
    <p> Good day</p>
    <br>
    <p>Click the button to verify</p>
    <br>
    <p>please verify your account </p>
    <button class="btn btn-success" type="submit> Verify </button>

    <h6>Thank You</h6>
    </div>"""

    
    message = MessageSchema(
    subject=" Account Verification",
    recipients=user_email,
    body=html,
    subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


# @router.post("/email")
# async def TaskNotification(email: EmailSchema) -> JSONResponse:
#         html = f"""
#     <div class="container>
#     <p>{content.subject}</p>
#     <br>
#     <p> Good day</p>
#     <br>
#     <p>{content.message}</p>
#     <br>
#     <p>please verify your account </p>
#     <button class="btn btn-success" type="submit> Verify </button>

#     <h6>Thank You</h6>
#     </div>"""

    
#     message = MessageSchema(
#     subject="Fastapi-Mail module",
#     recipients=recepiants.model_dump().get("email"),
#     body=html,
#     subtype=MessageType.html)

#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent"})