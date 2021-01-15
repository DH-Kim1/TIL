import pprint
import requests

# API 요청 URL을 확인한다. (+ 필요한 데이터 넘겨주기)
name = 'ruby'
url = f'https://api.nationalize.io/?name={name}'
# url ? name=asjdlkfj 이런형태를 query string 쿼리스트링

response = requests.get(url).json() 
# 괄호가 붙는건 메서드(기능)을 실행시킨다 라는 의미
#괄호가 없으면 데이터를 꺼내는 

# pprint.pprint(response)

# print(f'{name}님의 예상 국적은 {national} 입니다.')

# 응답결과 확인 후 정보 추출하기
name = response['name']
# 해당결과에서 리스트형식의 첫번째 딕셔너리를 불러와야 하므로 [0]번째 리스트항목을 불러오기
country_id = response['country'][0]['country_id']
probability = round(response['country'][0]['probability'] * 100, 2)

# 최종 결과값 출력
print(f'{name}의 국적은 {probability}% 확률로 {country_id}입니다')