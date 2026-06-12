from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#remove windows warning messages
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#change path to where your have it!
se = Service(executable_path=<YOUR chromedriver.exe>)
driver = webdriver.Chrome(service=se,options=options)
driver.get("https://www.shopsite.com/demo.html")

username_box = driver.find_element(By.ID,"username")
username_box.click()

seremail_box = driver.find_element(By.ID,"useremail")
useremail_box.click()
useremail_box.send_keys("bla@bla.com")

