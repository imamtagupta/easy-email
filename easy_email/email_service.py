from config import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class EmailService:
    def __init__(self) -> None:
        self.smtp_server = settings("smtp_server")
        self.smtp_port = settings("smtp_port")
        self.email = settings("email")
        self.password = settings("password")
        self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)

    def message_setup(self, subject, body, bodyType):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, bodyType))
        return msg

    def sever_up(self):
        self.server.starttls()
        self.server.login(self.email, self.password)

    def server_down(self):
        self.server.quit()

    def send_to(self, msg, recipients):
        self.sever_up()
        for recipient in recipients:
            msg['To'] = recipient
            text = msg.as_string()
            self.server.sendmail(self.email, recipient, text)
            print(f"Email sent to {recipient}")
        self.server_down()