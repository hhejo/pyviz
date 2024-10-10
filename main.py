# from dotenv import load_dotenv
import os
# from collections import Counter, defaultdict
from selenium_controller import crawl_texts
from mbti_controller import  get_mbti_counts
from mbti_wordcloud import create_wordcloud
from file_controller import load_csv, save_csv, save_txt

# load_dotenv()

file_path = os.path.join('assets', 'mbti_counts.csv')
if os.path.isfile(file_path):
  print('크롤링하지 않고 csv 파일을 읽기')
  mbti_counts = load_csv('assets/mbti_counts.csv')
else:
  scroll_counts = 3
  start_sec, end_sec = 3.2, 5.7
  titles, contents = crawl_texts(scroll_counts, start_sec, end_sec)
  mbti_counts = get_mbti_counts(titles, contents)
  create_wordcloud(mbti_counts)
  save_csv('assets/mbti_counts.csv', mbti_counts)
  save_txt('assets/titles.txt', titles)
  save_txt('assets/contents.txt', contents)
print('MBTI 통계: ', mbti_counts)
