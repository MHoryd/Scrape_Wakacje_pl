# Scrape_Wakacje_pl_Project

This is my first web scraping project where I aim to generate for me reports composed of opportunities of cheap vacations. Program is scraping polish portal wakacje.pl and then selects from scraped data those offers which match filtering criteria.

For this web scparing project i am using Python libraries BeautifulSoup and Selenium.

To configure search, program is opening search_params.json file which need to have list of dictionaries in following format:
[
    {
        "filtering_params":{
            "max_price" : 1111,
            "min_duration" : 1
        },
        "scrape_params":{
            "country":"name",
            "date_from":"1111-11-11",
            "date_to":"1111-11-11",
            "stay_length":"11-11",
            "stars":"4-gwiazdkowe"    
        }

    }
]
For each dictionary object program will scrape wakacje.pl. Url for this search is composed based on scrape_params. Later, data are filtered based on filtering_params. If program will find matching offers, html report will be produced.
