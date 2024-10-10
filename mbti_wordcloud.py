from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

font_path = '/Library/Fonts/AppleGothic'
background_color = 'white'
colormap = 'Accent_r'
width = 800
height = 800
# max_words=100
# stopwords=STOPWORDS


def create_wordcloud(mbti_counts):
  wordcloud = WordCloud(font_path=font_path, background_color=background_color, colormap=colormap, width=width, height=height)
  wordcloud = wordcloud.generate_from_frequencies(mbti_counts)
  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.title('MBTI 언급량')
  plt.savefig('assets/mbti_wordcloud.png')
  print('워드클라우드가 mbti_wordcloud.png 파일로 저장되었습니다.')
  plt.close()

# # 시각화
# wordcloud = wordcloud.generate(words)
# # wordcloud_words = wordcloud.generate_from_frequencies(word)
# array = wordcloud.to_array()

# 제외 단어 설정
# from wordcloud import STOPWORDS
# STOPWORDS.add('가산', '맛', '메뉴')
