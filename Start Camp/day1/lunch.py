menu = ['예향정', '장가계', '첨단공원국밥']
#print(menu)
#print(menu[0])

phone_book = {'예향정': '123-123', '첨단공원국밥': '456-456', '장가계': '789-789'}
# print(phone_book)
# print(phone_book['첨단공원국밥'])


#1. 가게 하나 랜덤으로 추천받기 random.choice를 통해 구현해보기
import random

my_menu = random.choice(menu)
#print(my_menu + '의 전화번호는' + phone_book[my_menu] + ' 입니다') # + 연산자를 통하여 붙여넣을 수 있음

print(f'오늘의 점심메뉴는 {my_menu}!! {phone_book[my_menu]}') # f를 따옴표 앞에 붙이고 my_menu를 중괄호로 감싸줌
#위에서 사용한 f는 f-string라는 기능으로 파이선 3.6버전 이후부터 지원
# f-string을 사용하여 문자열을 연결하여 사용 가능

