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


def create_plot(file_name, mbti_counts):
  mbti_types = list(mbti_counts.keys())
  counts = list(mbti_counts.values())
  plt.figure(figsize=(10, 6))
  colors = ['skyblue' if mbti.startswith('E') else 'tomato' for mbti in mbti_types]
  plt.bar(mbti_types, counts, color=colors)
  plt.title('MBTI 언급량', fontsize=14)
  plt.xlabel('MBTI', fontsize=12)
  plt.ylabel('횟수', fontsize=12)
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig(file_name)
  plt.close()
  print(f'{file_name} 저장 완료')


def create_wordcloud(file_name, mbti_counts):
  def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    if word.startswith('E'):
      return 'skyblue'
    elif word.startswith('I'):
      return 'tomato'
  # wordcloud = WordCloud(font_path=font_path, background_color=background_color, colormap=colormap, width=width, height=height)
  wordcloud = WordCloud(font_path=font_path, background_color=background_color, color_func=color_func, width=width, height=height)
  wordcloud = wordcloud.generate_from_frequencies(mbti_counts)
  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.title('MBTI 언급량')
  plt.savefig(file_name)
  plt.close()
  print(f'{file_name} 저장 완료')
