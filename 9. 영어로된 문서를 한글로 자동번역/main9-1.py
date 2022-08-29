import googletrans # 구글 번역기 사용을 위한 라이브러리 설치 필요

translator = googletrans.Translator() # 번역모듈을 변수에 바인딩


# translate 함수 사용
str1 = "행복하세요" 
result1 = translator.translate(str1, dest='en', src='auto') 
print(f"행복하세요 => {result1.text}") 

str2 = "I am happy" 
result2 = translator.translate(str2, dest='ko', src='auto') 
print(f"I am happy => {result2.text}")

