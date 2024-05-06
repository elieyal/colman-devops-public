from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = Options()
options = [
  "--headless",
  "--disable-gpu",
  "--window-size=1920,1200",
  "--ignore-certificate-errors",
  "--disable-extensions",
  "--no-sandbox",
  "--disable-dev-shm-usage"
]

for option in options:
  chrome_options.add_argument(option)

def test_site():
  url = "http://localhost"

  se = ChromeService(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=se,options=chrome_options)

  driver.get(url)

  btn1 = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[1]/button").click()
  btn_plus = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[4]/button").click()
  btn2 = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[2]/button").click()
  btn_eql = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[5]/div[3]/button").click()
  result = driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div").text

  print(result)
  driver.quit()
  assert result == "3", "Wrong result"
