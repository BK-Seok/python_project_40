from os import linesep
import googletrans

translator = googletrans.Translator() 

read_file_path = r"9. 영어로된 문서를 한글로 자동번역\영어파일.txt"
write_file_path = r"9. 영어로된 문서를 한글로 자동번역\한글파일.txt"
# 저장할 경로와 파일이름 지정

with open(read_file_path, 'r') as f : 
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko') 
    print(result1.text)
    # a: 추가 모드, 존재하는 파일에 추가할 때 사용하며 파일이 없다면 생성합니다.
    with open(write_file_path,'a', encoding='UTF8') as f:
        f.write(result1.text + '\n') # 한줄씩 저장
        print(type(write_file_path))