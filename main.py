import os
from controllers.selenium_controller import crawl_texts
from controllers.mbti_controller import  get_mbti_counts
from controllers.plot_controller import create_plot, create_wordcloud, create_specific_plot
from controllers.file_controller import load_csv, save_csv, save_txt


def exec_crawl(scroll_counts, min_wait_sec, max_wait_sec):
    csv_file_path = os.path.join('assets', 'mbti_counts.csv')  # /assets/mbti_counts.csv 파일 위치
    mbti_counts = {}  # MBTI별 언급량 {MBTI_타입: 개수}
    if os.path.isfile(csv_file_path):
        print('저장된 데이터 사용')
        mbti_counts = load_csv('assets/mbti_counts.csv')  # 저장된 파일이 있으면 크롤링하지 않고 해당 csv 파일 사용
        create_plot('assets/mbti_plot.png', mbti_counts)  # MBTI 언급량으로 막대 그래프 생성하고 저장
        create_specific_plot('assets/mbti_plot.png', mbti_counts)
        create_wordcloud('assets/mbti_wordcloud.png', mbti_counts)  # MBTI 언급량으로 워드 클라우드 생성하고 저장
    else:
        titles, contents = crawl_texts(scroll_counts, min_wait_sec, max_wait_sec)  # 게시글 제목, 내용 크롤링 (스크롤 횟수, 최소 대기시간, 최대 대기시간)
        mbti_counts = get_mbti_counts(titles, contents)  # 크롤링한 제목, 내용으로부터 MBTI 언급량 얻기
        create_plot('assets/mbti_plot.png', mbti_counts)  # MBTI 언급량으로 막대 그래프 생성하고 저장
        create_specific_plot('assets/mbti_plot.png', mbti_counts)
        create_wordcloud('assets/mbti_wordcloud.png', mbti_counts)  # MBTI 언급량으로 워드 클라우드 생성하고 저장
        save_csv('assets/mbti_counts.csv', mbti_counts)  # MBTI 언급량을 CSV 파일로 저장
        save_txt('assets/titles.txt', titles)  # 제목 모음을 txt 파일로 저장
        save_txt('assets/contents.txt', contents)  # 내용 모음을 txt 파일로 저장

    print('MBTI 언급량: ', mbti_counts)
    return


if __name__ == '__main__':
    exec_crawl(3, 1.5, 2.2)
