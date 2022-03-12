from gmail import Gmail
from message import Message

from dotenv import load_dotenv
from os import getenv

# load data from .env file
load_dotenv()


#Logowanie
mailer = Gmail(
    username=getenv('_USERNAME'),
    password=getenv('_PASSWORD'),
    host='smtp.gmail.com',
    port=465
)
mailer.login()

mess = Message()

mailer.send_mail(
    recipent_email='informatyka@pszczyna.edu.pl',
    subject='Prezentacja JS testy jednostkowe',
    content=mess.render(),
    file='C:\\Users\\Ja\\Desktop\\prezentacja_brodacz_QUnit.odp'
)
