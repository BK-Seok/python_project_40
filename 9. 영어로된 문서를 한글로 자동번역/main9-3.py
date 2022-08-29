from os import linesep
import googletrans

translator = googletrans.Translator() 

# 번역할 텍스트 파일 경로 바인딩
read_file_path = r"9. 영어로된 문서를 한글로 자동번역\영어파일.txt"

# r: 읽기 모드, 파일을 읽을 때 사용합니다.
# w: 쓰기 모드, 파일에 쓸 때 사용하며 파일이 이미 동일한 이름으로 존재한다면 덮어씁니다.
# a: 추가 모드, 존재하는 파일에 추가할 때 사용하며 파일이 없다면 생성합니다.
# r+, w+, a+: 읽기모드 + 쓰기모드
# rb, wb, ab, rb+, wb+, ab+: 각각의 모드들은 위와 동일하나 Binary 포맷으로 읽거나 쓰는걸 진행합니다.
with open(read_file_path, 'r') as f : # 파일열기 모드중 read 모드의 open 함수를 변수로 바인딩
    readLines = f.readlines() # 한 줄씩 리스트 타입의 데이터를 원소로 받아오는 함수를 바인딩
print(readLines)
print(readLines.__class__) # 데이터 타입 확인
print(type(readLines))

for lines in readLines:
    result1 = translator.translate(lines, dest='ko') 
    print(result1.text)
