from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
import re, os
from selenium.webdriver.chrome.service import Service
from scrape_script.selenium_helpers import Selenium_Helpers
from scrape_script.url_generator import Url_generator


privacy_agreement_button_xpath = "//button[contains(text(),'AKCEPTUJĘ I PRZECHODZĘ DO SERWISU')]"
all_offers_on_page_xpath = "//a[@data-test-offer-id]"
pagination_div_xpath = "//div[@data-area='pagination']"
next_page_button_xpath = "//a[@type='next']"
page_bottom_xpath = "//div[@data-area='center']"
no_results_found_xpath = "//p[contains(text(),'Nie znaleźliśmy ofert, które spełniają wszystkie wybrane kryteria.')]"


class Scrape_wakacje_pl:


    def __init__(self, param):
        self.URL_object = Url_generator(**param)
        self.URL = self.URL_object.format_url()
        self.deals_dictionary_list = []
        self.s = Service('/usr/lib/chromium-browser/chromedriver')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        

    def get_results_from_page(self, vacations_offers):
            for offer in vacations_offers:
                new_offer = {}
                link = offer.get_attribute('href')
                new_offer['offer_link']= link
                elementHTML = offer.get_attribute('outerHTML')
                element_soup = BeautifulSoup(elementHTML, 'html.parser')
                price_div = element_soup.find('div', {'data-testid':'offer-listing-section-price'})
                price_extracted = re.findall('[0-9]', price_div.text)
                price_int = int(''.join(price_extracted))
                new_offer['price'] = price_int
                date_span = element_soup.find('span', {'data-testid':'offer-listing-duration-date'})
                start_date_string, end_date_string = date_span.text.split('- ')
                start_date = datetime.strptime(start_date_string, '%d.%m.%Y')
                end_date = datetime.strptime(end_date_string, '%d.%m.%Y')
                formatted_start_date = start_date.strftime('%Y-%m-%d')
                formatted_end_date = end_date.strftime('%Y-%m-%d')
                new_offer['start_date'] = formatted_start_date
                new_offer['end_date'] = formatted_end_date
                duration_span = element_soup.find('span', {'data-testid':'offer-listing-duration-day'})
                duration_extracted = re.findall('[0-9]', duration_span.text)
                duration_int = int(''.join(duration_extracted))
                new_offer['duration'] = duration_int
                self.deals_dictionary_list.append(new_offer)


    def scrape(self):
        if os.name == 'posix':
            self.driver = webdriver.Chrome(service=self.s, options=self.options)
        else:
            self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.maximize_window()
        SH = Selenium_Helpers(self.driver)
        elem = SH.locate_elem_by_xpath(xpath=privacy_agreement_button_xpath)
        elem.click()
        no_results_found_by_provided_params = SH.assess_is_any_matching_vacations_on_page(no_results_found_xpath=no_results_found_xpath)
        if no_results_found_by_provided_params:
            self.driver.quit()
            return False
        Continue_click_next = True
        while Continue_click_next:
            Continue_scroll_down = True
            while Continue_scroll_down:
                SH.locate_elem_by_xpath(xpath='//picture')
                base_elem = SH.locate_elem_by_tag_name(tag='body')
                base_elem.send_keys(Keys.PAGE_DOWN)
                Continue_scroll_down = SH.assess_do_scroll_down(xpath=page_bottom_xpath)
                if Continue_scroll_down == False:
                    try:
                        vacations_offers = SH.locate_elems_by_xpath(xpath=all_offers_on_page_xpath)
                        self.get_results_from_page(vacations_offers)
                        elem = SH.locate_elem_by_xpath(xpath=next_page_button_xpath)
                        if elem == False:
                            Continue_click_next=False
                            self.driver.quit()
                        else:
                            elem.click()
                    except StaleElementReferenceException:
                        pass
        return self.deals_dictionary_list