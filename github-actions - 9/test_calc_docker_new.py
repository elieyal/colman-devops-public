from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

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
  webdriver_path = 'C:\\Users\\eliey\\Desktop\\chromedriver_win32\\chromedriver.exe'

  se = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
  driver = webdriver.Chrome(service=se,options=chrome_options)

  driver.get(url)

  btn1 = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[3]/button").click()
  btn_plus = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[6]/button").click()
  btn2 = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[4]/div[4]/button").click()
  btn_eql = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[5]/div[3]/button").click()
  result = driver.find_element(By.XPATH,"//*[@id='root']/div/div[1]/div[2]").text
  print(result)
  driver.quit()
  assert result == "3", "Wrong result"
