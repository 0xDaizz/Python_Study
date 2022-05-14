from lib2to3.pgen2.driver import Driver
from selenium import webdriver

Driver = webdriver.Chrome()
Driver.get("https://naver.com")


# brew로 크롬드라이버 설치했더니 이게 되네;;;
