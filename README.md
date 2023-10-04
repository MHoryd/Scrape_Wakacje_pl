# Scrape_Wakacje_pl_Project

This is my first web scraping project where I aim to generate reports composed of opportunities for cheap vacations. The program scrapes Polish portal wakacje.pl and if search params return offers, it composes html report and and it to selected emails.

For this web scparing project i am using Python libraries BeautifulSoup and Selenium.

To configure search, program is opening search_params.json file which need to have list of dictionaries in following format:
```
[
    {

        "country":"name",
        "date_from":"1111-11-11",
        "date_to":"1111-11-11",
        "stay_length":"1-11",
        "stars":"4-gwiazdkowe",
        "max_price": 1111,
        "transportation":"samolotem",
        "amenities":"all-inclusive",
        "depature_city":"Some City"

    }
    
    ]
```

For each dictionary object program will scrape wakacje.pl. Url for this search is composed based on scrape_params.