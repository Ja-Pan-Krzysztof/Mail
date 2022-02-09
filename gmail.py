from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Gmail:
    def __init__(self, username: str, password: str, host: str, port: int):
        self.username = username
        self.password = password

        self.server = SMTP_SSL(host, port)

    def login(self):
        self.server.ehlo()
        self.server.login(self.login, self.password)

    def send_mail(self, recipent_email: str, subject: str, content: str):
        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = self.username
        message['To'] = recipent_email
        message.attach(
            MIMEText(content, 'html')
        )

        self.server.sendmail(self.username, recipent_email, message.as_string())

    def __del__(self):
        self.server.close()







