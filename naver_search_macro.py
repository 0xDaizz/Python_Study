from selenium import webdriver
import time

url = 'http://naver.com'

driver = webdriver.Chrome('/Users/hw/Desktop/python_study/chromedriver')  
#구버전? 작동되긴 하는데 deprecated되었다고 뜸
#executable_path has been deprecated, please pass in a Service object

driver.get(url)

time.sleep(3)

#--------------

find = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input')
#요것도 바뀐 것 같음
#find_element_by_xpath is deprecated. Please use find_element(by=By.XPATH, value=xpath) instead


find.clear()

find.send_keys("비트코인 가격")

search = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button/span[2]')

search.click()

time.sleep(2)

driver.close()




# 참고 사이트 
# https://blog.naver.com/ree31206/222396021285
# https://awintersky.tistory.com/8?category=759576
# https://blog.naver.com/jsk6824/221763151860
# https://blog.naver.com/jsk6824/221768421554
# https://blog.naver.com/jsk6824/221752099024

# 개꿀사이트
# https://blog.naver.com/dktmrorl/222671592303