import pyautogui as pag
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 절대경로로 바꿨을 때 발생하는 오류 발생시 \  >>  \\
# 이미지를 이용하여 포인트 찾을 수 있다

picPosition = pag.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\1.PNG')
print(picPosition)

# locateOnScreen 이미지의 위치를 Box형식으로 반환
if  picPosition is None:
    picPosition = pag.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\2.PNG')
    print(picPosition)

if  picPosition is None:
    picPosition = pag.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\3.PNG')
    print(picPosition)