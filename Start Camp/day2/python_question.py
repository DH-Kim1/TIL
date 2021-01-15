import pprint
# hpy.hk/mini-practice-1

# 미니 실습1

# 1-1. 자신의 이름, 나이, 인사말로 구성된 my_info dictionary를 만들어보시오.
# (name, age, msg)
my_info = {
    'name': '김대호',
    'age': 29,
    'msg': 'SSAFY 5기 화이팅',
}

#1-2. my_info 딕셔너리에서 나이만 출력하시오.
# print(my_info)
# print(my_info['age'])

# 미니 실습2 Value 안에 또 dictionary가 있음

coin = {
    "BTC": {
        "opening_price": "44405000",
        "closing_price": "38806000",
        "min_price": "36640000",
        "max_price": "44999000",
        "prev_closing_price": "44404000",
        "fluctate_24H": "-7463000",
        "fluctate_rate_24H": "-16.13"
    },
    "ETH": {
        "opening_price": "1458000",
        "closing_price": "1229000",
        "min_price": "1100000",
        "max_price": "1490000",
        "prev_closing_price": "1458000",
        "fluctate_24H": "-275000",
        "fluctate_rate_24H": "-18.28"
    },
    "XRP": {
        "opening_price": "364.5",
        "closing_price": "311.9",
        "min_price": "284.2",
        "max_price": "372.7",
        "prev_closing_price": "364.2",
        "fluctate_24H": "-90.6",
        "fluctate_rate_24H": "-22.51"
    }
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오. coin에서 BTC꺼내는것처럼 max_price도 그대로 꺼내기
# pprint.pprint(coin['BTC']['max_price'])

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
btc_opening_price = int(coin['BTC']['opening_price']) # 정수는 int()내장함수를 이용하여 사용
xrp_opening_price = float(coin['XRP']['opening_price']) # 실수는 float()라는 내장함수를 가져와서 바꿔주어야 함

total_opening_price = btc_opening_price + xrp_opening_price

# print(btc_opening_price)
# print(xrp_opening_price)
# print(total_opening_price)
# print(type(total_opening_price))

# hpy.hk/list-dict-dummy
# 

movie = {
    "movieInfo": {
        "movieNm": "광해, 왕이 된 남자",
        "movieNmEn": "Masquerade",
        "showTm": "131",
        "prdtYear": "2012",
        "openDt": "20120913",
        "typeNm": "장편",
        "nations": [
            {
            "nationNm": "한국"
            }
        ],
        "genres": [
            {
            "genreNm": "사극"
            },
            {
            "genreNm": "드라마"
            }
        ],
        "directors": [
            {
            "peopleNm": "추창민",
            "peopleNmEn": "CHOO Chang-min"
            }
        ],
        "actors": [
            {
            "peopleNm": "이병헌",
            "peopleNmEn": "LEE Byung-hun",
            "cast": "광해/하선"
            },
            {
            "peopleNm": "류승룡",
            "peopleNmEn": "RYU Seung-ryong",
            "cast": "허균"
            },
            {
            "peopleNm": "한효주",
            "peopleNmEn": "HAN Hyo-joo",
            "cast": "중전"
            }
        ]
    }
}

# 1. 영화의 제목을 출력하시오.
print(movie['movieInfo']['movieNm'])


# 2. 다음 movie의 감독의 영어 이름을 출력하시오. directors는 리스트이므로 [0]번째
print(movie['movieInfo']['directors'][0]['peopleNmEn'])

# 3. 다음 movie의 배우의 인원을 출력하시오. len()함수를 이용하여 리스트 개수를 셀 수 있다.
print(len(movie['movieInfo']['actors']))