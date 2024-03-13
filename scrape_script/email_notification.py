from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os


class Email_notifi():
    

    def __init__(self,mail_config):
        self.sender = mail_config.notification_email
        self.receivers = mail_config.notification_receivers_email
        self.password = mail_config.notification_pass
        self.smtp_server = mail_config.notification_smtp_server


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
            for receiver in self.process_receivers(self.receivers):
                msg = self.create_message(receiver).as_string()
                server.sendmail(self.sender,receiver,msg)
            server.quit()
        except Exception as e:
            print(f"Error: Unable to establish an SMTP connection{datetime.now()}")
            print(e, flush=True)

    def process_receivers(self, receivers):
        if ',' in receivers:
            receivers_list = receivers.split(',')
            return receivers_list
        else: 
            return [receivers]
