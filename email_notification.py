from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os

class Email_notifi():
    
    def __init__(self):
        self.sender = os.environ.get('Notification_email')
        self.receivers = os.environ.get('Notification_receivers_email').split(',')
        self.password = os.environ.get('Notification_pass')
        self.smtp_server = os.environ.get('Notification_smtp_server')

    def create_message(self, receiver):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = receiver
        msg['Subject'] = f"Wakacje PL scrape {datetime.now().date()}"
        body = "The attachments contain information about offers that meet the criteria."
        msg.attach(MIMEText(body, 'plain'))
        for filename in os.listdir('./Reports'):
            file_path = os.path.join('./Reports', filename)
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(file_path, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")
            msg.attach(part)
        return msg

    def send_message(self):
        try:
            server = SMTP(self.smtp_server)
            server.starttls()
            server.login(self.sender, self.password)
            for receiver in self.receivers:
                msg = self.create_message(receiver).as_string()
                server.sendmail(self.sender,receiver,msg)
            server.quit()
        except Exception as e:
            print(f"Error: Unable to establish an SMTP connection{datetime.now()}")
            print(e)
