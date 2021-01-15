greeting = '안녕하세요!!'

#1. while문 반복 (ctrl / 하면 선택한 줄은 다 주석처리됨)
# count = 0
# while count < 5:
#     print(greeting)
#     count = count + 1

#2. for문 반복
# count_list = [0, 1, 2, 3]
# for num in count_list:
#     print(num)
#     print(greeting)

#3. for문 반복(함수활용-range라는 빌트인함수를 활용하여 범위만큼 반복되게 함)
for num in range(4):
    print(greeting)

#*빌트인함수는 아무런 작업없이 바로 쓸 수 있는 함수
#range, len, print 등등 파이썬 내에 이미 만들어져있는 함수

#1. Non Built in Function 빌트인함수가 아닌 경우 함수가 포함된 코드를 불러온다. (import)
#2. 함수를 사용한다
#예제 - random.choice(리스트)
