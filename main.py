import os
from controller.selenium_controller import crawl_texts
from controller.mbti_controller import  get_mbti_counts
from controller.plot_controller import create_plot, create_wordcloud
from controller.file_controller import load_csv, save_csv, save_txt

file_path = os.path.join('assets', 'mbti_counts.csv')
mbti_counts = {}
if os.path.isfile(file_path):
  print('저장된 데이터 사용')
  mbti_counts = load_csv('assets/mbti_counts.csv')
else:
  scroll_counts = 500
  start_sec, end_sec = 2, 3.5
  titles, contents = crawl_texts(scroll_counts, start_sec, end_sec)
  mbti_counts = get_mbti_counts(titles, contents)
  create_plot('assets/mbti_plot.png', mbti_counts)
  create_wordcloud('assets/mbti_wordcloud.png', mbti_counts)
  save_csv('assets/mbti_counts.csv', mbti_counts)
  save_txt('assets/titles.txt', titles)
  save_txt('assets/contents.txt', contents)

print('MBTI 통계: ', mbti_counts)
