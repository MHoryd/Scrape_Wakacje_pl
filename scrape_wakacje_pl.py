from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
import re
from selenium.webdriver.chrome.service import Service


privacy_agreement_button_xpath = "//button[contains(text(),'AKCEPTUJĘ I PRZECHODZĘ DO SERWISU')]"
all_offers_on_page_xpath = "//a[@data-test-offer-id]"
pagination_div_xpath = "//div[@data-area='pagination']"
next_page_button_xpath = "//a[@type='next']"
page_bottom_xpath = "//div[@data-area='center']"
no_results_found_xpath = "//p[contains(text(),'Nie znaleźliśmy ofert, które spełniają wszystkie wybrane kryteria.')]"


class Scrape_wakacje_pl:

    def __init__(self, **kwarg):
        self.country = kwarg['country']
        self.date_from = kwarg['date_from']
        self.date_to = kwarg['date_to']
        self.stay_length = kwarg['stay_length']
        self.stars = kwarg['stars']
        self.URL = f'https://www.wakacje.pl/wczasy/{self.country}/?od-{self.date_from},do-{self.date_to},{self.stay_length}-dni,samolotem,all-inclusive,{self.stars},z-warszawy&src=fromFilters'
        self.deals_dictionary_list = []
        self.s = Service('/usr/lib/chromium-browser/chromedriver')
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        

    def locate_elem_by_xpath(self, xpath, time_to_wait = 5):
        try:
            elem = WebDriverWait(driver=self.driver,timeout=time_to_wait).until(ec.visibility_of_element_located((By.XPATH,xpath)))
            return elem
        except TimeoutException:
            return False

    def locate_next_page_button_by_xpath(self, xpath, time_to_wait = 5):
        try:
            elem = WebDriverWait(driver=self.driver,timeout=time_to_wait).until(ec.visibility_of_element_located((By.XPATH,xpath)))
            return elem.is_displayed()
        except TimeoutException:
            return False


    def locate_elem_by_tag_name(self, tag, time_to_wait = 5):
        try:
            elem = WebDriverWait(driver=self.driver,timeout=time_to_wait).until(ec.visibility_of_element_located((By.TAG_NAME, tag)))
            return elem
        except TimeoutException:
            return False

    def locate_elems_by_xpath(self, xpath, time_to_wait = 5):
        try:
            elems = WebDriverWait(driver=self.driver,timeout=time_to_wait).until(ec.presence_of_all_elements_located((By.XPATH,xpath)))
            return elems
        except TimeoutException:
            return False
    
    def assess_do_scroll_down(self, xpath, time_to_wait = 0.5):
        try:
            WebDriverWait(driver=self.driver, timeout=time_to_wait).until(ec.presence_of_element_located((By.XPATH, xpath)))
            return False
        except TimeoutException:
            return True
        
    def assess_is_any_matching_vacations_on_page(self, time_to_wait = 0.5):
        try:
            WebDriverWait(driver=self.driver, timeout=time_to_wait).until(ec.visibility_of_element_located((By.XPATH, no_results_found_xpath)))
            return True
        except TimeoutException:
            return False

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
        self.driver = webdriver.Chrome(service=self.s, options=self.options)
        self.driver.get(self.URL)
        self.driver.maximize_window()
        elem = self.locate_elem_by_xpath(privacy_agreement_button_xpath)
        elem.click()
        no_results_found_by_provided_params = self.assess_is_any_matching_vacations_on_page()
        if no_results_found_by_provided_params:
            self.driver.quit()
            return False
        Continue_click_next = True
        while Continue_click_next:
            Continue_click_next = True
            Continue_scroll_down = True
            while Continue_scroll_down:
                self.locate_elem_by_xpath('//picture')
                base_elem = self.locate_elem_by_tag_name('body')
                base_elem.send_keys(Keys.PAGE_DOWN)
                Continue_scroll_down = self.assess_do_scroll_down(page_bottom_xpath)
                if Continue_scroll_down == False:
                    try:
                        vacations_offers = self.locate_elems_by_xpath(all_offers_on_page_xpath)
                        self.get_results_from_page(vacations_offers)
                        elem = self.locate_elem_by_xpath(next_page_button_xpath)
                        if elem == False:
                            Continue_click_next=False
                            self.driver.quit()
                        else:
                            elem.click()
                    except StaleElementReferenceException:
                        pass
        return self.deals_dictionary_list
