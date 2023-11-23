import requests, re
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime
from scrape_script.url_generator import Url_generator



class Scrape_wakacje_pl:


    def __init__(self, param):
        self.param = param
        self.URL_object = Url_generator(**self.param)
        self.URL_object.format_url()
        self.deals_dictionary_list = []

    def scrape(self):
        sesion = requests.session()
        request = sesion.get(self.URL_object.url)
        soup_object = BeautifulSoup(request.text, 'html.parser')
        offers_not_found = soup_object.find('div', {'data-testid':'NotificationBannerWrapper'})
        if offers_not_found:
            return False
        script_tags = soup_object.find_all('script')
        target_tag = script_tags[4]
        reg = re.findall('"count":(\d+)', str(target_tag))
        offers_number = int(reg[1])
        while offers_number > 0:
            self.URL_object.add_next_page_num_to_url()
            offers_number -= 10
            print(self.URL_object.url)
            request = sesion.get(self.URL_object.url)
            soup_object = BeautifulSoup(request.text, 'html.parser')
            root_elem = etree.HTML(str(soup_object))
            offers = root_elem.xpath('//a[@data-test-offer-id]')
            for offer in offers:
                new_offer = {}
                stay_length_elem = offer.xpath(".//span[@data-testid='offer-listing-duration-date']")
                stay_length_text_content = ''.join(etree.XPath("string()")(stay_length_elem[0]))
                start_date_string, end_date_string = stay_length_text_content.split('- ')
                start_date = datetime.strptime(start_date_string, '%d.%m.%Y')
                end_date = datetime.strptime(end_date_string, '%d.%m.%Y')
                formatted_start_date = start_date.strftime('%Y-%m-%d')
                formatted_end_date = end_date.strftime('%Y-%m-%d')
                new_offer['start_date'] = formatted_start_date
                new_offer['end_date'] = formatted_end_date
                price_elem = offer.xpath(".//div[@data-testid='offer-listing-section-price']//text()")
                new_offer['price'] = int(''.join([digit for digit in price_elem[1] if digit != ' ']))
                duration_length_elem = offer.xpath(".//span[@data-testid='offer-listing-duration-day']/text()")
                new_offer['duration'] = int(duration_length_elem[1])
                raw_offer_href = offer.get('href')
                new_offer['offer_link']= f"https://www.wakacje.pl/{raw_offer_href}/?od-{formatted_start_date},{int(duration_length_elem[1])}-dni,{self.param['amenities']}{self.param['departure_city']}"
                self.deals_dictionary_list.append(new_offer)

        return self.deals_dictionary_list