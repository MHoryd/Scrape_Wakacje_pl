from scrape_wakacje_pl import Scrape_wakacje_pl
from filter_results import FilterResults
from report_generator import ReportGenerator
from email_notification import Email_notifi
from file_manager import file_manager
import json



class ScrapeControler:


    def run(self):
        FM = file_manager()
        FM.check_is_report_dir_present()
        with open('search_params.json', mode='r') as f:
            params = json.load(f)

        for param in params:
            Scrape_object = Scrape_wakacje_pl(**param['scrape_params'])
            scrapped_data = Scrape_object.scrape()
            if scrapped_data:
                filtered_result = FilterResults(scrapped_data,param['filtering_params'])
                if filtered_result.match_list:
                    report = ReportGenerator(filtered_result.match_list,param)
                    report.compose_report()
                    report.finalize_and_save_report()
        if FM.reports_files_presence_check():
            EN = Email_notifi()
            EN.send_message()
            FM.delete_report_files()

if __name__ == '__main__':
    SC = ScrapeControler()
    SC.run()
