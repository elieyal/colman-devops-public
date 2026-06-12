from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#remove windows warning messages
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#change path to where your have it!
se = Service(executable_path='C:\\Users\\eliey\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=se,options=options)
driver.get("https://www.shopsite.com/demo.html")

purchases = driver.find_element(By.CSS_SELECTOR,".nav > li:nth-child(3) > a:nth-child(1)").click()