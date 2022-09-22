import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_button(browser):
    browser.get(link)
    #time.sleep(600)
    button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert len(button) == 1, f"Assertion error: found {len(button)} elements, expected 1!"