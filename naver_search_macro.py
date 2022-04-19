from selenium import webdriver
import time

url = 'http://naver.com'

driver = webdriver.Chrome('/Users/hw/Desktop/python_study/chromedriver')  #구버전? 작동되긴 하는데 deprecated되었다고 뜸
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

