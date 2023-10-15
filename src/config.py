import os
from dotenv import load_dotenv

load_dotenv(".env")

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
  CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
  CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
  MAIL_USERNAME =os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  MAIL_FROM = os.environ.get("MAIL_FROM")
  MAIL_PORT = 465
  MAIL_SERVER = os.environ.get("MAIL_SERVER")
  MAIL_STARTTLS = False
  MAIL_SSL_TLS = True
  USE_CREDENTIALS = True
  VALIDATE_CERTS = True
