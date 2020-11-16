import unittest
from selenium import webdriver
from time import sleep


class MercadoLibreSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.get('https://www.mercadolibre.com.co/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_ps4(self):
        driver = self.driver

        search_bar = driver.find_element_by_xpath('/html/body/header/div/form/input')
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys('playstation 4')
        search_bar.submit()
        sleep(3)

        model = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/dl[3]/dd[1]/a/span[1]')
        model.click()
        sleep(3)

        condition = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[3]/dl[7]/dd[1]/a/span[1]')
        condition.click()
        sleep(3)

        dropdown_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        dropdown_menu.click()
        sleep(3)

        higher_price = driver.find_element_by_class_name('andes-list__item-text')
        higher_price.click()
        sleep(5)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text()
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div/div/div/span[1]/span[2]').text()
            prices.append(article_price)

        print(articles, prices)    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)