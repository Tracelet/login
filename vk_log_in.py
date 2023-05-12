import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from config import password, email


driver = webdriver.Chrome()

for i in range(5):
    try:
        driver.get("https://vk.com/login")
    except WebDriverException as e:
        print(e.msg)
        if i == 4:
            exit(1)
        time.sleep(1)

for i in range(10):
    try:
        email_input = driver.find_element(By.ID, 'index_email')
    except NoSuchElementException as e:
        print(e.msg)
        if i == 9:
            exit(1)
        time.sleep(1)

email_input.send_keys(email)
email_input.send_keys(Keys.ENTER)
time.sleep(5)

for i in range(10):
    try:
        pass_input = driver.find_element(By.NAME, 'password')
    except NoSuchElementException as e:
        print(e.msg)
        if i == 9:
            exit(1)
        time.sleep(1)

pass_input.send_keys(password)
pass_input.send_keys(Keys.ENTER)
time.sleep(10)

owner = driver.find_element(By.ID, 'owner_page_name')
assert owner.text == "Егор Рожковский"
post = driver.find_element(By.ID, 'wpt198676138_512')
print(post.text)
