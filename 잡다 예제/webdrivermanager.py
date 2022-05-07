from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://opensea.io")
# webdrivermanager를 이용해서 크롬드라이버 셀레니움 구동하는 방법


