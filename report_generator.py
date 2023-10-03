from datetime import datetime
import os

class ReportGenerator:


    def __init__(self, data, param):
        self.data = data
        self.param_country_name = param["scrape_params"]["country"]
        self.param_country_price = param["filtering_params"]["max_price"]
        self.param_country_min_duration = param["filtering_params"]["min_duration"]
        self.current_date = datetime.now().date()
        self.html_template = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        font-family: Arial, sans-serif;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin-bottom: 10px;
        border: 1px solid #ddd;
        padding: 10px;
        background-color: #f9f9f9;
    }
    a {
        text-decoration: none;
        color: #333;
    }
</style>
</head>
<body>
    <ul>
"""


    def check_is_report_dir_present(self):
        if os.path.exists('./Reports') == False:
            os.mkdir('./Reports')

    def compose_report(self):
        for item in self.data:
            offer_link = item['offer_link']
            price = item['price']
            start_date = item['start_date']
            end_date = item['end_date']
            duration = item['duration']

            self.html_template += f"""
            <li>
                <p>Price: {price}, start_date: {start_date}, end_date: {end_date}, duration: {duration}</p><a href='{offer_link}'>{offer_link}</a>
            </li>"""

    def finalize_and_save_report(self):
        self.html_template += """
                            </ul>
                        </body>
                        </html>
                        """
        with open(f"Reports/scrapped_data_{self.param_country_name}_{self.param_country_price}_{self.param_country_min_duration}_{self.current_date}.html", "w") as file:
            file.write(self.html_template)