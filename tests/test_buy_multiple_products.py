import time

import pytest
# import pages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.checkout_complete_page import Checkout_complete_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_information_page import Payment_information_page
from pages.user_information_page import User_information_page

users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'

@pytest.mark.run(order=3)
def test_buy_product_1():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    print('Start test 1')
    login_page = Login_page(driver)
    login_page.authorization(user=users[0], password=password)
    mp = Main_page(driver)
    mp.add_sauce_labs_backpack_to_cart()
    cp = Cart_page(driver)
    cp.click_on_checkout_button()
    print('Test finished')
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order=1)
def test_buy_product_2():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    print('Start test 2')
    login_page = Login_page(driver)
    login_page.authorization(user=users[0], password=password)
    mp = Main_page(driver)
    mp.add_sauce_labs_bike_light_to_cart()
    cp = Cart_page(driver)
    cp.click_on_checkout_button()
    print('Test finished')
    time.sleep(5)
    driver.quit()

@pytest.mark.run(order=2)
def test_buy_product_3():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    print('Start test 3')
    login_page = Login_page(driver)
    login_page.authorization(user=users[0], password=password)
    mp = Main_page(driver)
    mp.add_sauce_labs_bolt_t_shirt_to_cart()
    cp = Cart_page(driver)
    cp.click_on_checkout_button()
    print('Test finished')
    time.sleep(5)
    driver.quit()
