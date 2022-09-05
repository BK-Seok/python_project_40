import requests
import re


url = 'https://www.news1.kr/articles/?4794363&kakao_from=mainnews' 

headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
        }

response = requests.get(url, headers=headers)

results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text) 

results = list(set(results))

print(results)