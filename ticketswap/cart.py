"""Defines Cart"""

# import os
from subprocess import Popen

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class Cart(object):
    FACEBOOK_URL = "https://www.facebook.com"
    TICKETSWAP_URL = "https://www.ticketswap.com/login"

    def __init__(self, url):
        self.url = url
        self.driver = self.__init_chrome()

    def authorize(self, user, password):
        self.__auth_on_facebook(user, password)
        self.__auth_on_ticketswap()
        self

    def add(self):
        self

    # Private section

    def __init_chrome(self):
        process = Popen(["which", "chromedriver"])
        path = process.communicate()[0]
        # TOOD: raise an error if path is empty
        return webdriver.Chrome(path)

    def __auth_on_facebook(self, user, password):
        self.driver.get(self.FACEBOOK_URL)
        assert "Facebook" in self.driver.title
        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys(user)
        pass_input = self.driver.find_element_by_id("pass")
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.RETURN)

    def __auth_on_ticketswap(self):
        self.driver.get(self.TICKETSWAP_URL)

    def __click_on_item(self):
        ticket_item = self.driver.find_element_by_class_name("listings--items")
        ticket_item.click()

    def __buy_ticket(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until( # noqa
            expected_conditions.element_to_be_clickable((By.ID, 'listing-reserve-form'))
        )

        buy_elem = self.driver.find_element_by_css_selector(
            '#listing-reserve-form > input.btn.btn-success.btn-lg.btn-buy'
        )
        buy_elem.click()

# def add_ticket(url):
#     """Add a ticket to your ticketswap cart."""
#     login_url = 'https://www.ticketswap.com/login'
#     driver_path = os.path.join(os.getenv('HOME'), 'bin', 'chromedriver')
#     driver = webdriver.Chrome(driver_path)

#     usr = os.getenv('FB_user')
#     pwd = os.getenv('FB_password')

#     driver.get("http://www.facebook.com")
#     assert "Facebook" in driver.title
#     elem = driver.find_element_by_id("email")
#     elem.send_keys(usr)
#     elem = driver.find_element_by_id("pass")
#     elem.send_keys(pwd)
#     elem.send_keys(Keys.RETURN)

#     #  Login
#     driver.get(login_url)
#     driver.get(url)
#     ticket_elem = driver.find_element_by_class_name("listings--items")
#     ticket_elem.click()

#     wait = WebDriverWait(driver, 10)
#     element = wait.until( # noqa
#         expected_conditions.element_to_be_clickable((By.ID, 'listing-reserve-form'))
#     )

#     buy_elem = driver.find_element_by_css_selector(
#         '#listing-reserve-form > input.btn.btn-success.btn-lg.btn-buy'
#     )
#     buy_elem.click()
