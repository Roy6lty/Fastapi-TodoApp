from typing import List
from .config import Config
from fastapi import BackgroundTasks, FastAPI, APIRouter
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, select_autoescape, PackageLoader
from abc import ABC, abstractmethod


class EmailSchema(BaseModel):
    email: List[EmailStr]

class EmailContent(BaseModel):
    message:str
    subject: str

templates = Jinja2Templates(directory="templates")


env = Environment(
    loader=PackageLoader('src', '../templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

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

class Email(ABC):
    @abstractmethod
    def __init__(self, recipientsemail: List):
        self.recipient = recipientsemail
       
        

    def message(self):
        MessageSchema(subject=self.subject, recipients=self.recipientsemail)

    
class VerficationEmail(Email):
    def __init__(self, recipient: str, username: str, url:str):
        super().__init__(recipient)
        self.username = username
        self.url = url
        

     # Generate the HTML template base on the template name
    def get_template(self):
        template = env.get_template('verification.html')
        return template


    def message(self)->MessageSchema:
        template = self.get_template()
        html = template.render(url=f"127.0.0.1:8000/verification/email/{self.url}", 
                               first_name=self.username)
        
        message = MessageSchema(
            subject= "Account Verification",
            recipients= [self.recipient],
            body= html,
            subtype= MessageType.html)
        
        return message
    

class LoginNotificationEmail(Email):
    def __init__(self, url: str, recipient: str | List, subject: str, body):
        super().__init__(url, recipient, subject, body)


    

class SendEmail:
    def __init__(self, email:Email):
         self.email = email
        

    async def sendemail(self):
        fm = FastMail(conf)
        await fm.send_message(self.message())
        return JSONResponse(status_code=200, content={"message": "email has been sent"})






router = APIRouter()

@router.post("/email_test")
async def TestEmail(recipient:str, url:str, username:str):
    verification = VerficationEmail( 
                     recipient=recipient,
                     url=url,
                     username=username)
    await SendEmail.sendemail(verification)
    return "Email Successful"

# template = env.get_template('verification.html')

# html = template.render(
#         url=url, #link for button
#         first_name=name,
#         subject=subject
#         )

# @router.post('/email/testmail/')
# async def TestMail(content:EmailContent, recipients:EmailSchema):
    
#     html = templates.render(
#         first_name = "John",
#         subject = content.subject,
#         url="localhost/verifiction/email/{token}"

#     )
        
#     message = MessageSchema(
#     subject=content.subject,
#     recipients=recipients.model_dump().get('email'),
#     body=html.render(url='https://example.com/confirm'),
#     subtype=MessageType.html)

#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent"})


# @router.post('/email/verification//')
# async def VerificationSendEmail(user_email:str, content: EmailContent):

#     html = f"""
#     <div class="container>
#     <p> Good day</p>
#     <br>
#     <p>Click the button to verify</p>
#     <br>
#     <p>please verify your account </p>
#     <button class="btn btn-success" type="submit> Verify </button>

#     <h6>Thank You</h6>
#     </div>"""

    
#     message = MessageSchema(
#     subject=" Account Verification",
#     recipients=user_email,
#     body=html,
#     subtype=MessageType.html)

#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent"})


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