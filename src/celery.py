from celery import shared_task
from celery.contrib.abortable import AbortableTask
from dotenv import load_dotenv
from time import sleep
from .config import Config

from celery import Celery

from typing import List

from fastapi import BackgroundTasks, FastAPI, APIRouter
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse

load_dotenv(".env")

celery =Celery(__name__)
celery.conf.broker_url = Config.CELERY_BROKER_URL
celery.conf.result_backend = Config.CELERY_RESULT_BACKEND


conf = ConnectionConfig(
    MAIL_USERNAME = Config.MAIL_USERNAME,
    MAIL_PASSWORD = Config.MAIL_PASSWORD,
    MAIL_FROM = Config.MAIL_FROM,
    MAIL_PORT = 465,
    MAIL_SERVER = Config.MAIL_SERVER,
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
)

@shared_task(bind=True, base=AbortableTask)
def countdown(self, count:int):
    for i in range(count):
        print(i)
        sleep(1)
        if self.is_aborted():
            return 'TASK STOPPED'
        return "Done"

@shared_task(bind=True, base=AbortableTask)
async def VerificationSendEmail(self, user_email:str, content: str):

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
    if self.is_aborted():
            return 'TASK STOPPED'
    return "Verifiaction sent"



