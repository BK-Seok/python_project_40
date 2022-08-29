import pyautogui
import pyperclip
import time
import schedule
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_mesaage():
    picPosition = pyautogui.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\1.PNG')
    print(picPosition)

    if  picPosition is None:
        picPosition = pyautogui.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\2.PNG')
        print(picPosition)

    if  picPosition is None:
        picPosition = pyautogui.locateOnScreen('C:\python project 40\\11. 오토마우스를 활용한 PC카카오톡 자동화\\3.PNG')
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

# schedule 모듈을 이용하여 10초당 메세지를 전송을 실행
schedule.every(10).seconds.do(send_mesaage)

while True:
    schedule.run_pending()  #무한루프를 돌면서 1초에 한번씩 스케쥴을 지속적으로 체크
    time.sleep(1)