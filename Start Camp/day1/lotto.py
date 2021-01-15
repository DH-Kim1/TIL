import random #import문은 스크립트파일 최상단에 위치하는것으로

#2. random.sample(리스트, 개수)
#리스트에서 특정 수의 요소를 임의적으로 비 복원추출
#예제 random 활용해서 로또추첨기 만들어보기

#(1) 1번부터 45번까지의 숫자를 만들어 저장하기
numbers = range(1, 46) #뒷번호는 원하는 숫자보다 +1 해주어야함
#print(numbers)

#(2)numbers에서 6개숫자를 뽑아서 저장하기
lucky_numbers = random.sample(numbers, 6)
print(sorted(lucky_numbers)) # 숫자를 작은것부터 정렬해보자 -> sorted()함수를 이용

#프로그래밍 언어의 3형식
#1. 저장
#2. 조건
#3. 반복 while, for

