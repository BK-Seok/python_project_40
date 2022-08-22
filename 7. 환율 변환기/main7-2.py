from currency_converter import CurrencyConverter    # 환율 계산 라이브러리

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
print(cc.convert(1,'USD','KRW'))    # 데이터 타입 변환 함수