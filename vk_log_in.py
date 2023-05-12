import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from config import password, email


def check_element(by: str, element: str):

    for i in range(10):
        try:
            driver.find_element(by, element)
        except NoSuchElementException as e:
            print(f"Try to found element \"{element}\" by {by}...       {i + 1}/ 10")
            if i == 9:
                raise e.msg
            time.sleep(1)
        else:
            break


driver = webdriver.Chrome()

for i in range(5):
    try:
        driver.get("https://vk.com/login")
    except WebDriverException as e:
        if i == 4:
            raise e
        time.sleep(1)
    else:
        break

check_element(By.ID, 'index_email')

email_input = driver.find_element(By.ID, 'index_email')
email_input.send_keys(email)
email_input.send_keys(Keys.ENTER)
time.sleep(5)

check_element(By.NAME, 'password')
pass_input = driver.find_element(By.NAME, 'password')
pass_input.send_keys(password)
pass_input.send_keys(Keys.ENTER)
time.sleep(10)

check_element(By.ID, 'owner_page_name')
owner = driver.find_element(By.ID, 'owner_page_name')
assert owner.text == ""
check_element(By.ID, 'wpt198676138_512')
post = driver.find_element(By.ID, 'wpt198676138_512')
print(post.text)
