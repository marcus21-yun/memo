import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# # movies (tr들) 의 반복문을 돌리기
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if a_tag is not None:
#         # a의 text를 찍어본다.
#         print (a_tag.text)
#
#
#
# test = soup.select_one('a[href="/movie/point/af/list.nhn?st=mcode&sword=171539"]')
# # select를 이용해서, 순위, 영화별철들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')
# # print(movies)

rank = 1

for movie in movies:
    title_tag = movie.select_one(".title")
    rate_tag = movie.select_one('td.point')
    if title_tag != None:
        print(rank, title_tag.text.strip(),rate_tag.text)
        rank += 1

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.point