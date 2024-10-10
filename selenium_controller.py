from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import ssl
import time
import random


def init_selenium():
  ssl._create_default_https_context = ssl._create_unverified_context
  chrome_options = Options()
  chrome_options.add_experimental_option('detach', True)
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  chrome_options.add_argument('--no-sandbox')  # 리소스 보호 모드 비활성화 (권장 옵션)
  chrome_options.add_argument('--disable-dev-shm-usage')  # 메모리 문제 방지 (권장 옵션)
  Service(executable_path=ChromeDriverManager().install())
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def crawl_texts(scroll_counts, start_sec, end_sec):
  base_url = 'https://www.teamblind.com/kr/topics/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95'
  driver = init_selenium()
  driver.get(base_url)
  driver.implicitly_wait(15)
  start = 0
  titles, contents = [], []
  for i in range(scroll_counts):
    title_elements = driver.find_elements(By.CSS_SELECTOR, '.article-list-pre .tit h3 > a')
    for title_element in title_elements[start:]:
      titles.append(title_element.text.upper())
    content_elements = driver.find_elements(By.CSS_SELECTOR, '.article-list-pre .tit p > a')
    for content_element in content_elements[start:]:
      contents.append(content_element.text.upper())
    print(f'{i + 1} 제목 / 내용: {len(titles)} / {len(contents)}')
    action = driver.find_element(By.CSS_SELECTOR, 'body')
    action.send_keys(Keys.END)
    if i == 0:
      start += 32
    start += 20
    sleep_time = round(random.uniform(start_sec, end_sec), 3)
    time.sleep(sleep_time)
  return titles, contents
