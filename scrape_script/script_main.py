from scrape_script.scrape_wakacje_pl import Scrape_wakacje_pl
from scrape_script.report_generator import ReportGenerator
from scrape_script.email_notification import Email_notifi
from scrape_script.file_manager import file_manager
from scrape_script.Mail_Config import MailConfig


class ScrapeControler:

    def __init__(self,params):
        self.params = params


    def run(self):
        FM = file_manager()
        FM.check_is_report_dir_present()


        for param in self.params:
            Scrape_object = Scrape_wakacje_pl(param)
            scrapped_data = Scrape_object.scrape()
            if scrapped_data:
                report = ReportGenerator(scrapped_data,param)
                report.compose_report()
                report.finalize_and_save_report()
        

        if FM.reports_files_presence_check():
            CM = MailConfig()
            mail_config = CM.get_config()
            if mail_config:
                EN = Email_notifi(mail_config)
                EN.prepare_reports_to_send()
                EN.send_message()
                FM.delete_report_files()