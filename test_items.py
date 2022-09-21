import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_web_ru(browser):
    browser.get(link)
    #time.sleep(600)
    browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')