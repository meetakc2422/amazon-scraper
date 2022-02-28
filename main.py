from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from parsel import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
i = 1
def crawler(driver):
    global i
    while i <4:
        ps = Selector(text=driver.page_source)
        item_name  = ps.xpath('//div[@class="a-section a-spacing-small s-padding-left-small s-padding-right-small"]//h2/a/span/text()').getall()
        item_url =ps.xpath('//div[@class="a-section a-spacing-small s-padding-left-small s-padding-right-small"]//h2/a/@href').getall()
        next_page = ps.xpath('//span[@class="s-pagination-strip"]/a[last()]/@href').extract_first()
        abs_url = 'https://www.amazon.in'+ str(next_page)
        print(abs_url)
        driver.get(abs_url)
        print(item_name)
        print(item_url)
        i = i +1
        crawler(driver)


url = "https://www.amazon.in"
ser =Service('chromedriver.exe')

driver = webdriver.Chrome(service=ser)
driver.get(url)
driver.maximize_window()
sleep(2)
search_area = driver.find_element(By.XPATH, '//div[@class="nav-search-field "]/input').send_keys('mammy poko pants')
sleep(1)

click_btn  = driver.find_element(By.XPATH,'//div[@class="nav-search-submit nav-sprite"]//input')
click_btn.click()
sleep(2)
crawler(driver)


