import pyautogui
import pyperclip
import time
import os

# os모듈을 사용하여 현재 경로를 확인
# cwd = os.getcwd()
# print(cwd)
# 지정된 경로에 존재하는 파일과 디렉터리 목록을 구하는 함수
# list = os.listdir()
# print(list)
# print(len(list))

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
# change directory
# 특정 경로에 대해 절대 경로 얻기
# os.path.abspath(path)
# 경로 중 디렉토리명만 얻기
# os.path.dirname(path)
# 경로 중 파일명만 얻기
# os.path.basename(path)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(__file__)
picPosition = pyautogui.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\1.PNG')
print(picPosition)

if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\1.PNG')
    print(picPosition)

if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\1.PNG')
    print(picPosition)

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다~~") 
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)