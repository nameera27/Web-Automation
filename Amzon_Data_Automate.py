from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# define driver
driver= webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

# Search Item
search_bar = driver.find_element(by=By.XPATH,value='//*[@id="twotabsearchtextbox"]')
search_bar.send_keys("Laptop Bag")
sleep(1)
search_icon = driver.find_element(by=By.XPATH,value='//*[@id="nav-search-submit-button"]')
search_icon.click()
sleep(1)

selectBag=ActionChains(driver).send_keys(Keys.ARROW_DOWN*(16)).perform()
driver.implicitly_wait(5)
bag = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
bag.click()

driver.quit()