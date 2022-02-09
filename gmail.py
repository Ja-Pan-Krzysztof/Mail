from smtplib import SMTP_SSL
from email.message import EmailMessage

from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Gmail:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.PORT = 465
        self.HOST = 'smtp.gmail.com'







