import re

test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
ok@ . 
no.kr
"""

# re모듈 findall함수로 raw string에 해당하는 문자열 데이터를 리스트로 만든다
results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)
print(results)
print('-'*20)
# set함수로 집합 안에서 unique한 값을 가지고
# dict()와 같이 순서에 상관없이 원소로 저장한다
results=set(results)
print(results)
print('-'*20)
# list함수로 순서가 있고 수정 가능한 객체 집합
# 위의 문자열의 경우 ',' 구분없이 분리되었기 때문에
# findall, set 으로 정리가 필요
results=list(results)
print(results)
print('-'*20)
# results = list(set(results))

# print(results)