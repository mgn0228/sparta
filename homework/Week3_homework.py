import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for music in musics:
    # movie 안에 a 가 있으면,
    qwer = music.select_one('td.info > a.title.ellipsis')
    if qwer is not None:
        rank = music.select_one('td.number').text # img 태그의 alt 속성값을 가져오기
        title = qwer.text.lstrip()                                    # a 태그 사이의 텍스트를 가져오기
        singer = music.select_one('td.info > a.artist.ellipsis').text 
        s = rank.split()[0]
        print(s,title,singer)