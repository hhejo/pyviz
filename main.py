from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import urllib.request
import ssl
from bs4 import BeautifulSoup
import time
import os
import requests

# 설정
load_dotenv()
ssl._create_default_https_context = ssl._create_unverified_context
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options)

# 로그인
base_url = 'https://www.instagram.com'
driver.get(base_url)
driver.implicitly_wait(10)
login_id = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
login_id.send_keys(os.environ.get('ID'))
login_pwd = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
login_pwd.send_keys(os.environ.get('PW'))
login_id.send_keys(Keys.ENTER)
time.sleep(7)

# 게시물 목록
food_url = 'https://www.instagram.com/hoseofood/'
driver.get(food_url)
driver.implicitly_wait(10)



elements = driver.find_elements(By.CSS_SELECTOR, '._ac7v a')
for element in elements:
  print(element)
  element.click()
  driver.implicitly_wait(10)
  el = driver.find_element(By.CSS_SELECTOR, '._a9zs h1')
  print(el.text)
  driver.find_element(By.CSS_SELECTOR, '._abl-').click()
  time.sleep(1)
  print('----------------------------------------------------')
