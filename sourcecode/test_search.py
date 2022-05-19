import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search(self):
        driver = self.driver
        driver.get("https://www.techwithtim.net")
        self.assertIn('techwithtim', driver.title)
        elem = driver.find_element_by_name("s")
        elem.send_keys("python")
        elem.send_keys(Keys.RETURN)
        time.sleep(50)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


