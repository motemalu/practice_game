#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from time import sleep
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

print("出席コードを入力してください")
shussekicode=input()


browser=webdriver.Chrome("chromedriver.exe")

url='https://nishitech.ap-cloud.com/login?return_to=https%3A%2F%2Fnishitech.ap-cloud.com%2F'
browser.get(url)
#sleep(4)

elem_username=browser.find_element_by_id('user_id')
elem_username.send_keys('ユーザーネーム')

elem_password=browser.find_element_by_id('password')
elem_password.send_keys('パスワード'+ Keys.ENTER)

elem_shusseki=browser.find_element_by_id('toggle-menu-51')
elem_shusseki.click()

elem_shussekicode=browser.find_element_by_id('passcode')
elem_shussekicode.send_keys(shussekicode+Keys.ENTER)
sleep(1)
browser.quit()



