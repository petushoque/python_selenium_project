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

    # Getters
    def get_sauce_labs_backpack_add_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.loc_sauce_labs_backpack_add_button)))

    def get_shopping_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_shopping_cart_button)))
    # Actions
    def add_sauce_labs_backpack_to_cart(self):
        self.get_sauce_labs_backpack_add_button().click()
        print('Click on "Add to cart" button')
        self.get_shopping_cart_button().click()
        print('Open the shopping cart')
