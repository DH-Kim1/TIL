import requests # 요청을 보내고 응답을 받아오는 역할
import datetime
from bs4 import BeautifulSoup # 데이터를 추출하기 좋은 형태로 구조화 해주는 것

url = 'https://finance.naver.com/marketindex/'

# 요청 보내기
response = requests.get(url).text
#print(type(response))

# 응답받은 값을 추출하기 쉬운 형태로 구조화하기
soup = BeautifulSoup(response, 'html.parser')
#print(type(soup))

# 원하는 데이터 추출하기
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
now = datetime.datetime.now()

#print(exchange)
print(f'{now} 현재 원/달러 환율은 {exchange}원 입니다')

#exchangeList > li.on > a.head.usd > div > span.value