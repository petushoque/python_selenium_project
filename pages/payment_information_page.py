import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Payment_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    loc_finish_button = '//button[@id="finish"]'

    # Getters
    def get_finish_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.loc_finish_button)))

    # Actions
    def click_on_finish_button(self):
        self.get_finish_button().click()
        print('Click on "Finish" button')

    #Methods
    def confirm_payment(self):
        self.get_current_url()
        self.click_on_finish_button()