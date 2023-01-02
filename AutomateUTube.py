from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driv = webdriver.Chrome()
driv.get("https://www.youtube.com/")

searchbox = driv.find_element(by=By.XPATH,value='//input[@id="search"]')
searchbox.send_keys("CodeWithHarry")

icon = driv.find_element(by=By.XPATH,value='//*[@id="search-icon-legacy"]')
icon.send_keys(Keys.ENTER)
sleep(5)
driv.close()
driv.quit()