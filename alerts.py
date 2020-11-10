import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.get('http://magento-demo.lexiconn.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_compare_productcs_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        alert = driver.switch_to_alert()
        alert_text = alert.text

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

if __name__ == "__main__":
    unittest.main(verbosity = 2)