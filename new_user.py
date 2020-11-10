import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.get('http://magento-demo.lexiconn.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/a[3]/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/form/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled()) 
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)n

        first_name = driver.find_element_by_id('firstname')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subs = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subs.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys('test')
        driver.implicitly_wait(3)
        last_name.send_keys('test')
        driver.implicitly_wait(3)
        email_address.send_keys('test@testmail.com')
        driver.implicitly_wait(3)
        news_letter_subs.send_keys('test')
        driver.implicitly_wait(3)
        password.send_keys('test')
        driver.implicitly_wait(3)
        confirm_password.send_keys('test')
        driver.implicitly_wait(3)
        submit_button.click()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)