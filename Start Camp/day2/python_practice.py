# 1. rlch wkfygud
number = 3 #숫자
# print(number)
# print(type(number)) # 자료형을 확인할 수 있는 빌트인 함수 type()

string = '문자열' # 문자열
# print(string)
# print(type(string))

boolean = True # Boolean
# print(boolean)
# print(type(boolean))

string_number = '3' # 따옴표로 둘러싼 숫자는 문자열로
#print(string_number + 5) # 형이 달라서 타입에러
# print(int(string_number) + 5)

# 2. f-string (string interpolation) 문자열 안에 변수를 넣는 방법
name = '김창규'
# print('제 이름은 ' + name + '입니다.')
# print(f'제 이름은 {name}입니다.')

# 3. List
my_list = ['python', 'html', 'markdown']
# print(my_list[2], my_list)
#위의 문자열을 다른것으로 바꿀경우
my_list[2] = 'java' # 위치를 찾았으므로 다른것으로 바꿔줄 수 있음
# print(my_list[2], my_list)

# 4. Dictionary 이름표를 적고 : 값을 적고 , 
# // 리스트 마지막에도 ,를 적는건 trailing comma라고 함
# // 나중에 리스트를 추가할 경우 ,가 누락되는 경우가 있어서 붙여놔도 오류가 나지 않으니
age_dict = {
    '박소현': 25,
    '김지용': 63,
}

# 딕셔너리 요소(원소) 접근
# print(age_dict['김지용'])
# print(age_dict['박소현'])
# print(age_dict.get('김지용'))
# print(age_dict.get('박소현'))

# 딕셔너리 요소 변경하기

age_dict['김지용'] = 103
# print(age_dict['김지용'])

# 기초 연산자
# -산술 연산자

# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(33 / 11) # 나누기
# print(33 // 11) # 몫
# print(100 % 3) # 나머지
# print(2 ** 5) # 거듭제곱

# -비교 연산자
# print(5 == 5) # 5=5
# print(5 == '3') # string 3과 같느냐
# print( 5 != 3) # 같지않음
# print(5 >= 3)
# print(5 < 3)

# 조건문 만들기
n = 10
# 1. 주어진 양수 n이 홀수, 짝수인지 판단하여 출력하는 코드를 작성해라.

# if n % 2 ==1:
#     print('홀수')
# else:
#     print('짝수')

# 2. 주어진 숫자 n이 양수인지, 0인지, 음수인지 판단하여 출력하는 코드

# if n > 0:
#     print('양수입니다.')
# elif n == 0:
#     print('0입니다')
# else:
#     print('음수입니다.')

# 3. 반복문

# numbers = [1, 2, 3]
# for number in numbers:
#     print(number)

numbers = range(1, 10)
for number in numbers:
    # 숫자가 들어오면, 홀수인지 판단하여 출력한다.
    if number % 2 == 1:
        print(f'숫자 {number}은(는) 홀수입니다!')
    else:
        print('짝수는 싫어요')

# 숫자 'ㅇㅇㅇ'은 홀수입니다. 라고 출력해보기