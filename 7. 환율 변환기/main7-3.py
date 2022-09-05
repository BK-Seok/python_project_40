"""
man7-3.py
2022.03.16 수정사항
1. https://kr.investing.com 사이트의 개편됨 기존의 코드 동작안됨
2. containers = content.find('span', {'data-test': 'instrument-price-last'}) 로 코드 변경
"""
import requests         # 파이썬에서 크롤링을 하기 위해 사용되는 내장 라이브러리
from bs4 import BeautifulSoup
# from pyspark.sql import functions as F



def get_exchange_rate(target1, target2):
    print("-----currency pair-----")
    print(target1, 'and', target2)
    print("-----------------------")
# header 없이 접속하면 로봇으로 인식하여 정보를 받아올 수 없다
# 답에 대한 메타 데이터를 담고 있는 응답 헤더는 headers 속성을 통해 사전의 형태로 얻을 수 있다
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
# requests 라이브러리를 사용하여 사이트 접속
# requests, content - 서버로부터 수신한 내용을 표시하는 명령어
    response = requests.get("https://kr.investing.com/currencies/{}-{}".\
                        format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    # BeautifulSoup는 바이트 단위의 정보가 필요
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    # 사이트에 HTTP통신으로 서버로부터 들어오는 html 데이터 구조
    # <span class="text-2xl" data-test="instrument-price-last">1,339.43</span>
    # text는 수신한 byte단위의 데이터를 자동으로 decode 하여 사용자가 보기 좋게 만들어줌
    # 속성을 통해 UTF-8로 인코딩된 문자열을 얻을 수 있다
    # # content는 수신한 byte단위의 데이터를 있는 그대로 보여줌
    
    print(containers.text)
    # print(containers.json())
    # text로 정보를 읽으면 데이터가 손상될 수 있으므로, byte단위인 content로 읽어야만 한다
    
get_exchange_rate('usd', 'krw')