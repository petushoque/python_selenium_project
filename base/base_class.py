class Base():

    def __init__(self, driver):
        self.driver = driver

    # Methods
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)
