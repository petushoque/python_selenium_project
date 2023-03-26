import time
#import pages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.user_information_page import User_information_page

users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'

def test_auth_test():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    login_page = Login_page(driver)
    login_page.authorization(user=users[0], password=password)
    mp = Main_page(driver)
    mp.add_sauce_labs_backpack_to_cart()
    cp = Cart_page(driver)
    cp.click_on_checkout_button()
    uip = User_information_page(driver)
    uip.input_user_information()

#auth(users, password)