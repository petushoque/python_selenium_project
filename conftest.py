import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def set_up():
    print('Start')
    #s = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=s)
    #url = 'https://www.saucedemo.com/'
    #driver.get(url)
    #driver.maximize_window()
    yield
    #time.sleep(5)
    #driver.quit()
    print('Finish')

@pytest.fixture(scope='modul')
def set_group():
    print('Enter')
    yield
    print('Exit')