import time
#import pages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import Login_page


users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'

def test_auth_test():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    login_page = Login_page(driver)
    login_page.authorization(users=users, password=password)

#auth(users, password)