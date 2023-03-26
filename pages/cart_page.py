import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    loc_checkout_button = '//button[@id="checkout"]'

    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_checkout_button)))

# Actions
    def click_on_checkout_button(self):
        self.get_current_url()
        self.get_checkout_button().click()
        print('Click on "Checkout" button')
