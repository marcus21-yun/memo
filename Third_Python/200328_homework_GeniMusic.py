# 20.3/28 숙제목표
# https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309 에서 1~50위 굑을 크롤링
# 순위/곡 제목 / 가수 를 표시한다.

import re
import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# 순위 :#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# 곡 제목 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# 가수 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

# select를 이용해서, tr들을 불러오기
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# musics (tr들) 의 반복문을 돌리기
for music in musics:
    # 순위를 분리해서 가져온다.
    a_tag = music.select_one('td.number')
    ranking = a_tag.text
    rank = ranking.split(' ')[0]

    # 곡 제목을 좌우 공백을 제외해서 가져온다.
    title_tag = music.select_one('td.info > a.title ')
    title = title_tag.text

    # 가수를 좌우 공백을 제외해서 가져온다.
    singer_tag = music.select_one('td.info > a.artist')
    singer = singer_tag.text
    singer_1 = singer.strip()

    # 순위, 곡제목, 가수 명을 순차적으로 출력한다.
    print(rank.strip(),title.strip(),singer_1)



