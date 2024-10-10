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
from konlpy.tag import Okt

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
time.sleep(5)

# 게시물 목록
food_url = 'https://www.instagram.com/hoseofood/'
driver.get(food_url)
driver.implicitly_wait(10)

def get_article():
  return el.text

li = []

# 첫 게시글
element = driver.find_element(By.CSS_SELECTOR, '._ac7v a')
element.click()
driver.implicitly_wait(10)
element = driver.find_element(By.CSS_SELECTOR, '._a9zs h1')
li.append(element.text)

# 계속 다음 게시글 가져오기
COUNTS = 10
for _ in range(COUNTS):
  next_button = driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-')
  next_button.click()
  time.sleep(0.5)
  el = driver.find_element(By.CSS_SELECTOR, '._a9zs h1')
  li.append(el.text)

print(li)
str = ''.join(li)

okt = Okt()
result = okt.nouns(str)
print(result)
