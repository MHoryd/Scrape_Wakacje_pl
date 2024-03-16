from datetime import datetime
import os
import requests

class Email_notifi():
    

    def __init__(self,mail_config):
        self.sender = mail_config.notification_email
        self.receivers = mail_config.notification_receivers_email
        self.password = mail_config.notification_pass
        self.url = mail_config.notification_smtp_server


    def send_message(self):
        for receiver in self.process_receivers(self.receivers):
            try:
                attachments = self.prepare_reports_to_send()
                request = requests.post(
                    self.url,
                    auth=("api",f"{self.password}"),
                    files=[("attachment", (os.path.basename(file), open(file, "rb").read())) for file in attachments],
                    data={
                        "from":f'Wakacje report {self.sender}',
                        "to":[receiver],
                        "subject":f"Wakacje script run report {datetime.now().date()}",
                        "text":"The attachments contain information about offers that meet the criteria."
                        })
                request.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(e, flush=True)


    def process_receivers(self, receivers):
        if ',' in receivers:
            receivers_list = receivers.split(',')
            return receivers_list
        else: 
            return [receivers]
        

    def prepare_reports_to_send(self):
        reports_folder = "./Reports"
        return [os.path.join(reports_folder, file) for file in os.listdir(reports_folder)]