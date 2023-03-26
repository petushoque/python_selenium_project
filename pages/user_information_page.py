import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class User_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    loc_first_name_field = '//input[@id="first-name"]'
    loc_last_name_field = '//input[@id="last-name"]'
    loc_postal_code_field = '//input[@id="postal-code"]'
    loc_continue_button = '//input[@data-test="continue"]'

    # Getters
    def get_first_name_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_last_name_field)))

    def get_postal_code_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_postal_code_field)))
    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name_field().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name_field().send_keys(last_name)
        print('Input last name')

    def input_postal_code(self, postal_code):
        self.get_postal_code_field().send_keys(postal_code)
        print('Input postal code')

    def click_on_continue_button(self):
        self.get_continue_button().click()
        print('Click on "Continue" button')

    #Methods
    def input_user_information(self):
        self.get_current_url()
        self.input_first_name('John')
        self.input_last_name('Doe')
        self.input_postal_code('90210')
        self.click_on_continue_button()