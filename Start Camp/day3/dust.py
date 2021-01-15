# 공공데이터 API 활용실습 (대기오염정보)

# 1. 필요한 라이브러리 import하기
import requests, datetime, pprint

# 2. API URL 및 KEY값 확인

key = 'gl7Etm1hFc4AB9WI%2F0ghBCQ%2FtrNVSbUx3aQQVRA1wgNn0tPfdejV%2FCkMac3YDD2Ni7WNmqtzwbEieAhdmVt9Uw%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName=광주&returnType=json'

# 3. 요청 및 응답값 확인

response = requests.get(url).json()
# pprint.pprint(response)


# 4. 최종 출력 문자열
# '__의 미세먼지 농도는 __입니다. (측정소: ___)'
# 주의 dictionary 와 list 잘 구분해서 찾아가기
sido_name = response['response']['body']['items'][1]['sidoName']
pm10 = response['response']['body']['items'][1]['pm10Value']
station_name = response['response']['body']['items'][1]['stationName']

print(f'{sido_name}의 미세먼지 농도는 {pm10}입니다. (측정소: {station_name})')