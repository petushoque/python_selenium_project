import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    loc_username = 'user-name'
    loc_password = '//*[@id="password"]'
    loc_login_button = '//*[@id="login-button"]'

    # Getters
    def get_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.loc_username)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_login_button)))

    # Actions
    def input_username(self, username):
        self.get_username().send_keys(username)
        print('Input login')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_on_login_button(self):
        self.get_login_button().click()
        print('Click on Login button')

    def authorization(self, users, password):
        for u in users:
            try:
                self.driver.get(self.url)
                self.driver.maximize_window()

                self.get_current_url()

                self.input_username(u)
                self.input_password(password)
                self.click_on_login_button()

                self.assert_word(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/div[2]/span'))), 'Products')

                #inventory_page_title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/div[2]/span')))
                #assert inventory_page_title.text == 'Products'
                #print('User: ' + u + ' successfully logged in!')
                menu_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn')))
                menu_button.click()
                logout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
                logout_button.click()
            except selenium.common.exceptions.TimeoutException:
                print('User: ' + u + ' authorization failed')
                self.driver.refresh()
