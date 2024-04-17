import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
se = Service(executable_path='C:\\webdriver\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=se)

file = open("config.json","r")
data = json.load(file)

driver.get(data["url"])

driver.find_element(By.ID,"user-name").send_keys(data["locked_user"])
driver.find_element(By.ID,"password").send_keys(data["pass"])
driver.find_element(By.ID,"login-button").click()
try:
    err_btn = driver.find_elements(By.XPATH,"//h3[@data-test='error']")[0].text
    assert err_btn == "Epic sadface: Sorry, this user has been locked out.", "Wrong result"
except:
    print("somehow the user logged in")
    driver.quit()
    exit(1)

driver.get(data["url"])
driver.find_element(By.ID,"user-name").send_keys(data["std_user"])
driver.find_element(By.ID,"password").send_keys(data["pass"])
driver.find_element(By.ID,"login-button").click()
logo = driver.find_elements(By.CLASS_NAME,"app_logo")
try:
    assert logo[0].text == "Swag Labs"
except AssertionError:
    print("failed to be in the first page")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
try:
    assert cart == "1"
except AssertionError:
    print("failed to add first product to cart")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
try:
    assert cart == "2"
except AssertionError:
    print("failed to add second product to cart")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
try:
    assert cart == "3"
except AssertionError:
    print("failed to add third product to cart")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"remove-sauce-labs-bike-light").click()
cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
try:
    assert cart.text == "2"
except AssertionError:
    print("failed to remove product from cart")
    driver.quit()
    exit(1)

driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
driver.find_element(By.ID,"remove-sauce-labs-fleece-jacket").click()
cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
try:
    assert cart.text == "1"
except AssertionError:
    print("failed to remove product from cart in checkout page")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"checkout").click()
try:
    driver.find_element(By.ID,"continue")
except:
    print("failed to get to the checkout page")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"first-name").send_keys(data["customer_first_name"])
driver.find_element(By.ID,"last-name").send_keys(data["customer_last_name"])
driver.find_element(By.ID,"postal-code").send_keys(data["customer_zip"])
driver.find_element(By.ID,"continue").click()
final_price = driver.find_element(By.CLASS_NAME,"inventory_item_price").text
try:
    assert final_price == "$7.99"
except AssertionError:
    print("Price is not as it should be")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"finish").click()
final_header = driver.find_element(By.CLASS_NAME,"complete-header").text
try:
    assert final_header == "Thank you for your order!"
except:
    print("Could not finish the checkout process")
    driver.quit()
    exit(1)

driver.find_element(By.ID,"back-to-products").click()
logo = driver.find_elements(By.CLASS_NAME,"app_logo")
try:
    assert logo[0].text == "Swag Labs"
except AssertionError:
    print("failed to be in the first page")
    driver.quit()
    exit(1)

driver.quit()