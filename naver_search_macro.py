#from selenium import webdriver
#import time
#driver = webdriver.Chrome('/Users/hw/Desktop/python_study/chromedriver')  
#구버전? 작동되긴 하는데 deprecated되었다고 뜸
#executable_path has been deprecated, please pass in a Service object


from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


url = 'http://naver.com'
driver.get(url)

time.sleep(3)

#--------------검색창을 찾는 과정

from selenium.webdriver.common.by import By
#이게 꼭 있어줘야 By를 쓸 수 있음

#find = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input')
#요것도 바뀐 것 같음
#find_element_by_xpath is deprecated. Please use find_element(by=By.XPATH, value=xpath) instead

find = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input')


find.clear()    #이미 입력되어있는 부분 삭제

find.send_keys("삼성전자 주가") #입력하고 싶은 거 입력

#search = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button/span[2]')
#신버전으로 교체

search = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button/span[2]')
#검색 돋보기 위치 입력

search.click()  #클릭

time.sleep(2)

#-------------

samsung = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/section[1]/div[1]/div[2]/div[1]/div/h3/a/span[2]/strong')
# 삼전 주가 부분 긁어옴

print(" "*10)
print(" "*10)
print("-"*10)
print("￦", samsung.text)
print("-"*10)








# 참고 사이트 
# https://blog.naver.com/ree31206/222396021285
# https://awintersky.tistory.com/8?category=759576
# https://blog.naver.com/jsk6824/221763151860
# https://blog.naver.com/jsk6824/221768421554
# https://blog.naver.com/jsk6824/221752099024

# 개꿀사이트
# https://blog.naver.com/dktmrorl/222671592303