class Base():

    def __init__(self, driver):
        self.driver = driver

    # Methods
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    def assert_word(self, elem, word):
        elem_value = elem.text
        assert elem_value == word
        print('Successful assertion')
