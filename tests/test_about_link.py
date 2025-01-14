import time
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

def test_about_link():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    login_page = Login_page(driver)
    login_page.authorization(user=users[0], password=password)

    mp = Main_page(driver)
    mp.open_about_link()