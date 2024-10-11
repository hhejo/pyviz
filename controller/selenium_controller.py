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
    print('Selenium 초기화 시작')
    ssl._create_default_https_context = ssl._create_unverified_context  # SSL 인증서를 검증하지 않게 설정
    chrome_options = Options()  # Selenium 크롬 브라우저 옵션 객체
    chrome_options.add_experimental_option('detach', True)  # 브라우저를 종료하지 않고 계속 실행 상태로 유지
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 로그 출력 비활성화 (DevTools 로그 등)
    chrome_options.add_argument('--no-sandbox')  # 보호된 리소스 사용 제한 해제 (Docker나 리소스 제약 환경에서 사용)
    chrome_options.add_argument('--disable-dev-shm-usage')  # 공유 메모리 사용을 비활성화해 메모리 문제 방지 (리소스가 적은 환경에서 유용)
    Service(executable_path=ChromeDriverManager().install())  # ChromeDriver의 실행 경로를 설정 및 설치 (ChromeDriverManager를 이용해 자동 설치)
    driver = webdriver.Chrome(options=chrome_options)  # 옵션이 적용된 Selenium WebDriver 객체 생성. Chrome 브라우저 실행
    print('Selenium 초기화 완료')
    return driver


def crawl_texts(scroll_counts, min_wait_sec, max_wait_sec):
    driver = init_selenium()  # Selenium 초기화

    base_url = 'https://www.teamblind.com/kr/topics/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95'
    driver.get(base_url)  # base_url로 접속
    driver.implicitly_wait(15)  # 페이지 요소 로딩 대기
    print(f'연결 URL: {base_url}')

    start_element_index = 0  # 저장할 요소의 시작 인덱스
    titles, contents = [], []  # 제목 모음, 내용 모음

    # 스크롤 횟수만큼 크롤링
    for i in range(scroll_counts):
        title_selector = '.article-list-pre .tit h3 > a'  # 제목 요소 선택자
        title_elements = driver.find_elements(By.CSS_SELECTOR, title_selector)  # 제목 요소들 가져오기
        for title_element in title_elements[start_element_index:]:
            titles.append(title_element.text.upper())  # 대문자 처리한 제목 텍스트 추가

        content_selector = '.article-list-pre .tit p > a'  # 내용 요소 선택자
        content_elements = driver.find_elements(By.CSS_SELECTOR, content_selector)  # 내용 요소들 가져오기
        for content_element in content_elements[start_element_index:]:
            contents.append(content_element.text.upper())  # 대문자 처리한 내용 텍스트 추가

        print(f'{i + 1}/{scroll_counts} 제목, 내용: {len(titles)}, {len(contents)}')

        action = driver.find_element(By.CSS_SELECTOR, 'body')  # body 요소 가져오기
        action.send_keys(Keys.END)  # 화면 제일 아래로 내려가기 (스크롤하기)

        if i == 0:
            start_element_index += 32  # 첫 번째 크롤링이면 32개 추가 (처음 화면에 나타나는 게시물은 총 52개)
        start_element_index += 20  # 이후부터 스크롤 내릴 때마다 게시물 20개씩 추가

        sleep_time = round(random.uniform(min_wait_sec, max_wait_sec), 2)  # 최소 대기시간, 최대 대기시간 사이 무작위 소수점 2자리 대기시간
        time.sleep(sleep_time)  # 해당 시간만큼 대기

    return titles, contents
