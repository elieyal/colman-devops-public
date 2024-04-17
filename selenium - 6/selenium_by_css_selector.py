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

username_box = driver.find_element(By.ID,"username")
username_box.click()
username_box.send_keys("abcd")

useremail_box = driver.find_element(By.ID,"useremail")
useremail_box.click()
useremail_box.send_keys("bla@bla.com")

checkbox = driver.find_element(By.ID,"shareemail").click()

btn = driver.find_element(By.CSS_SELECTOR,".btn").click()
