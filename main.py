from scrape_wakacje_pl import Scrape_wakacje_pl
from filter_results import FilterResults
from report_generator import ReportGenerator
from email_notification import Email_notifi
import json



class ScrapeControler:


    def run(self):
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
        EN = Email_notifi()



if __name__ == '__main__':
    SC = ScrapeControler()
    SC.run()