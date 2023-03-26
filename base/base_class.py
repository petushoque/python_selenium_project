import datetime


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
        print('Successful word assertion')

    def assert_url(self, exp):
        get_url = self.driver.current_url
        assert get_url == exp
        print('Successful url assertion')

    def make_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot_name = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('../screen/' + screenshot_name)