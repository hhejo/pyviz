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


def create_specific_plot(file_name, mbti_counts):
    name, ext = file_name.split('.')
    file_name = name + '_specific.' + ext

    e, i = 0, 0
    n, s = 0, 0
    f, t = 0, 0
    j, p = 0, 0
    for mbti_type, count in mbti_counts.items():
        if 'E' in mbti_type:
            e += count
        else:
            i += count
    for mbti_type, count in mbti_counts.items():
        if 'N' in mbti_type:
            n += count
        else:
            s += count
    for mbti_type, count in mbti_counts.items():
        if 'F' in mbti_type:
            f += count
        else:
            t += count
    for mbti_type, count in mbti_counts.items():
        if 'J' in mbti_type:
            j += count
        else:
            p += count

    plt.figure(figsize=(10, 6))
    colors = ['skyblue', 'tomato', 'skyblue', 'tomato', 'skyblue', 'tomato', 'skyblue', 'tomato']
    plt.bar(['E', 'I', 'N', 'S', 'F', 'T', 'J', 'P'], [e, i, n, s, f, t, j, p], color=colors)
    plt.title('부분 MBTI 언급량', fontsize=14)
    plt.xlabel('E, I, N, S, F, T, J, P', fontsize=12)
    plt.ylabel('횟수', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(file_name)
    plt.close()
    print(f'{file_name} 저장 완료')
