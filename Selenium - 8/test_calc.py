from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def test_site():
  url = "http://localhost"
  webdriver_path = 'C:\\Users\\eliey\\Desktop\\chromedriver_win32\\chromedriver.exe'

  se = Service(webdriver_path)
  driver = webdriver.Chrome(service=se,options=options)
  driver.get(url)


  btn1 = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[1]/button").click()
  btn_plus = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[4]/button").click()
  btn2 = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[2]/button").click()
  btn_eql = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[5]/div[3]/button").click()
  result = driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div").text
  print(result)
  driver.quit()
  assert result == "2", "Wrong result"