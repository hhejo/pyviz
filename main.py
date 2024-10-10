from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from konlpy.tag import Okt
from dotenv import load_dotenv
import ssl
import time
import os
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc
# 
import urllib.request
from bs4 import BeautifulSoup
import requests

# 설정
load_dotenv()
ssl._create_default_https_context = ssl._create_unverified_context
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options)

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

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

texts = []

# 첫 게시글
article = driver.find_element(By.CSS_SELECTOR, '._ac7v a')
article.click()
driver.implicitly_wait(10)
detail = driver.find_element(By.CSS_SELECTOR, '._a9zs h1')
texts.append(detail.text)

# 계속 다음 게시글 가져오기
COUNTS = 20
for _ in range(COUNTS):
  next_button = driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-')
  next_button.click()
  time.sleep(0.3)
  detail = driver.find_element(By.CSS_SELECTOR, '._a9zs h1')
  texts.append(detail.text)

# 명사 추출
okt = Okt()
tokens = okt.nouns(''.join(texts))
print(tokens)

# # 빈도수 확인
# LENGTH = 30
# nouns_counter = Counter(tokens)
# top_nouns = dict(nouns_counter.most_common(LENGTH))
# print(top_nouns)

# 시각화
font_path = '/Library/Fonts/AppleGothic'
word = ' '.join(tokens)
# max_words=100
# stopwords=STOPWORDS
wordcloud = WordCloud(font_path, background_color='white', colormap='Accent_r', width=800, height=800)
wordcloud = wordcloud.generate(word)
# wordcloud_words = wordcloud.generate_from_frequencies(word)
array = wordcloud.to_array()
fig = plt.figure(figsize=(10, 10))
plt.imshow(array, interpolation='bilinear')
plt.axis('off')
plt.show()
fig.savefig('wordcloud.png')

# 제외 단어 설정
# from wordcloud import STOPWORDS
# STOPWORDS.add('가산', '맛', '메뉴')
