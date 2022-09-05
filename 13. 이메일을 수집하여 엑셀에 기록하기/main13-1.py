import re # 정규 표현식

test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

# 문자열 앞에 r을 붙이면 raw string
# str=r'My \n Love'
# print(str)
# My \n Love
results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string) 

print(results)