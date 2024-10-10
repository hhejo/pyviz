from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc
from openai import OpenAI
from dotenv import load_dotenv
import ssl
import time
import os
from collections import Counter, defaultdict
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

MBTIS = ('ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP')
mbtis = {key: 0 for key in MBTIS}

base_url = 'https://www.teamblind.com/kr/topics/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95'
driver.get(base_url)
driver.implicitly_wait(10)
START = 0
texts = []
for i in range(3):
  titles = driver.find_elements(By.CSS_SELECTOR, '.article-list-pre .tit h3 > a')
  for title in titles[START:]:
    texts.append(title.text.upper())
  print(f'데이터 수: {len(texts)}')
  actions = driver.find_element(By.CSS_SELECTOR, 'body')
  actions.send_keys(Keys.END)
  if i == 0:
    START += 32
  START += 20
  time.sleep(2)

for text in texts:
  print(text)
  for MBTI in MBTIS:
    if MBTI in text:
      mbtis[MBTI] += 1
print('mbtis: ', mbtis)

# I와 E


# # 첫 게시글
# article = driver.find_element(By.CSS_SELECTOR, '._ac7v a')
# article.click()
# driver.implicitly_wait(10)
# detail = driver.find_element(By.CSS_SELECTOR, '._a9zs h1')
# texts.append(detail.text)
# print(f'#001 post saved')

# # 계속 다음 게시글 가져오기
# COUNTS = 9
# for i in range(2, COUNTS + 1):
#   next_button = driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-')
#   next_button.click()
#   time.sleep(0.3)
#   detail = driver.find_element(By.CSS_SELECTOR, '._a9zs h1')
#   texts.append(detail.text)
#   order = str(i)
#   print(f'#{order.rjust(3, '0')} post saved')

# # # 명사 추출
# # okt = Okt()
# # print(texts)
# # tokens = okt.nouns(''.join(texts))

# # # 빈도수 확인
# # LENGTH = 30
# # nouns_counter = Counter(tokens)
# # top_nouns = dict(nouns_counter.most_common(LENGTH))
# # print(top_nouns)

# # # 시각화
# # font_path = '/Library/Fonts/AppleGothic'
# # words = ' '.join(tokens)
# # # max_words=100
# # # stopwords=STOPWORDS
# # wordcloud = WordCloud(font_path, background_color='white', colormap='Accent_r', width=800, height=800)
# # wordcloud = wordcloud.generate(words)
# # # wordcloud_words = wordcloud.generate_from_frequencies(word)
# # array = wordcloud.to_array()
# # fig = plt.figure(figsize=(10, 10))
# # plt.imshow(array, interpolation='bilinear')
# # plt.axis('off')
# # plt.show()
# # fig.savefig('wordcloud.png')

# # 제외 단어 설정
# # from wordcloud import STOPWORDS
# # STOPWORDS.add('가산', '맛', '메뉴')

# # 음식 이름 추출
# # print('\n\n'.join(texts))
# # msg = '''
# # 오늘의 메뉴입니다. 선선한 날씨에 푹 끓인 따끈한 황태뭇국 어떠세요? 가을 무와 황태채에서 나온 육수의 감칠맛으로 구수하고 맛있는 황태뭇국과,

# # 질 좋은 돼지고기를 잘 익은 김치와 함께 볶아 더욱 맛있는 한국인의 주찬 돼지김치두루치기,

# # 바삭하게 튀겨낸 프라임치킨너겟 & 달콤한 스윗칠리,

# # 철판에서 노릇하게 부친 메밀전병에 알싸한 맛의 파채를 올려 포인트를 준 파채메밀전병,

# # 매콤한 소스에 아삭한 콩나물과 채소가 듬뿍, 쫄면의 쫄깃한 식감이 만나 많은 분들께서 좋아하시는 쫄면,

# # 부추와 갖은 채소를 송송 다져 듬뿍 넣은 조림간장에 간이 잘 배어 자꾸자꾸 손이 가는 마약계란장조림과

# # 얼갈이와 부추를 겉절이 양념장에 정성스레 버무려 맛을 더한 얼갈이겉절이가 오늘의 메뉴입니다❤

# # #가산 #가산디지털단지구내식당 #독산역구내식당 #가산디지털단지맛집 #가산맛집추천 #가디점심 #맛집그램 #맛스타그램 #먹스타그램 #오늘밥상 #한끼 #회사밥 #구내식당 #구내식당그램 #구내식당맛집 #호서구내식당 #식판 #식판샷 #우주최강가성비
# # '''
# msg = ''.join(texts)
# msg = f'{msg}\n위에서 음식이름을 뽑아줘 줄마다 숫자, 대시 이런 거 쓰지 말고 한 줄에 음식이름 하나씩만 미사여구 붙이지 말고'
# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
# client = OpenAI(api_key=OPENAI_API_KEY)
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": msg}
#     ]
# )
# print(completion.choices[0].message.content)

# li = completion.choices[0].message.content.split('\n')
# dict = defaultdict(int)
