
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login(self):
        driver = self.driver
        driver.get ("https://id.zing.vn/v2/login?apikey=92140c0e46c54994812403f564787c14&data=b-gPXW_sCVhuWdw9aQ")
        email = driver.find_element_by_id("login_account")
        email.send_keys("tuanhoangit174")
        password = driver.find_element_by_id("login_pwd")
        password.send_keys("Tuanhoangit174")

        driver.find_element_by_class_name("zidsignin_btn").click()
        time.sleep(60)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()