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


def create_wordcloud(file_name, mbti_counts):
  wordcloud = WordCloud(font_path=font_path, background_color=background_color, colormap=colormap, width=width, height=height)
  wordcloud = wordcloud.generate_from_frequencies(mbti_counts)
  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.title('MBTI 언급량')
  plt.savefig(file_name)
  plt.close()
  print(f'{file_name} 저장 완료')
