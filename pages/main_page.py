import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    loc_sauce_labs_backpack_add_button = 'add-to-cart-sauce-labs-backpack'
    loc_shopping_cart_button = 'shopping_cart_container'
    loc_menu_button = '//button[@id="react-burger-menu-btn"]'
    loc_about_link = '//a[@id="about_sidebar_link"]'

    # Getters
    def get_sauce_labs_backpack_add_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.loc_sauce_labs_backpack_add_button)))

    def get_shopping_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.loc_shopping_cart_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_menu_button)))

    def get_about_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_about_link)))

    # Actions
    def add_sauce_labs_backpack_to_cart(self):
        self.get_current_url()
        self.get_sauce_labs_backpack_add_button().click()
        print('Click on "Add to cart" button')
        self.get_shopping_cart_button().click()
        print('Open the shopping cart')

    def click_on_menu_button(self):
        self.get_menu_button().click()
        print('Click on Menu button')

    def click_on_about_link(self):
        self.get_about_link().click()
        print('Click on About link')

    # Methods
    def open_about_link(self):
        self.get_current_url()
        self.click_on_menu_button()
        self.click_on_about_link()
        self.assert_url('https://saucelabs.com/')