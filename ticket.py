"""Adds ticket to cart."""

import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def add_ticket(url):
    """Add a ticket to your ticketswap cart."""
    login_url = 'https://www.ticketswap.com/login'
    driver_path = os.path.join(os.getenv('HOME'), 'bin', 'chromedriver')
    driver = webdriver.Chrome(driver_path)

    usr = os.getenv('FB_user')
    pwd = os.getenv('FB_password')

    driver.get("http://www.facebook.com")
    assert "Facebook" in driver.title
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)

    #  Login
    driver.get(login_url)
    driver.get(url)
    ticket_elem = driver.find_element_by_class_name("listings--items")
    ticket_elem.click()

    wait = WebDriverWait(driver, 10)
    element = wait.until( # noqa
        EC.element_to_be_clickable((By.ID, 'listing-reserve-form'))
    )

    buy_elem = driver.find_element_by_css_selector(
        '#listing-reserve-form > input.btn.btn-success.btn-lg.btn-buy'
    )
    buy_elem.click()
