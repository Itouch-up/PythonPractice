
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = r'C:\\Users\\Touchup\\Downloads\\chromedriver.exe'
# headless_option = webdriver.ChromeOptions()
# headless_option.add_argument('headless')
# headless_option.add_argument('disable-cpu')
# headless_option.add_argument('lang=ko_KR')
# driver=webdriver.Chrome(chromedriver,options=headless_option)
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.daum.net")

assert "Daum" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()

elem.send_keys("butter")
elem.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source
time.sleep(3)
h2s = driver.find_elements_by_css_selector(
    '#clusterResultUL > li > div > div > div > a')
for h2 in h2s:
    print(h2.text)
driver.quit()
