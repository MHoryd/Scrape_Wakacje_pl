from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec


class Selenium_Helpers:

    def __init__(self, driver):
        self.driver = driver


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
        
    def assess_is_any_matching_vacations_on_page(self, no_results_found_xpath, time_to_wait = 0.5):
        try:
            WebDriverWait(driver=self.driver, timeout=time_to_wait).until(ec.visibility_of_element_located((By.XPATH, no_results_found_xpath)))
            return True
        except TimeoutException:
            return False