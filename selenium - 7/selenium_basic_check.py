from selenium import webdriver
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#driver = webdriver.Chrome(executable_path='C:\\Users\\eliey\\Desktop\\chromedriver_win32\\chromedriver.exe')
#driver.get("https://google.com")

se = Service(executable_path='C:\\Users\\eliey\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(options=options,service=se)
driver.get("https://google.com")
