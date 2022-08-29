import pyautogui
import time
import pyperclip
# pyperclip : 컴퓨터의 클립보드로 텍스트를 보내거나 클립보드에서 텍스트를 가지고 올 수 있도록 하는 모듈

while True:
    print(pyautogui.position())
    time.sleep(0.1)

    pyautogui.moveTo(1700,360,0.2)

    # 절대값 좌표에 마우스 왼쪽 클릭
    # pyautogui.click(100, 100)
    # 현재 마우스 커서 위치에서 마우스 왼쪽 버튼 더블 클릭
    # pyautogui.doubleClick()
    # 현재 마우스 커서 위치에서 마우스 왼쪽 버튼 클릭
    # click()은 mouseDown(), mouseUp()이 합쳐진 함수
    # pyautogui.click()
    pyautogui.click()
    time.sleep(0.5)
    # 그림판에서 팬슬 선택 후 직선 그릴 때 (예)
    # 마우스 커서 x = 200, y = 200으로 이동
    # pyautogui.moveTo(200, 200)
    # 마우스 왼쪽 버튼 클릭
    # pyautogui.mouseDown()
    # 마우스 x = 300, y = 300으로 이동 (왼쪽 버튼 누른 상태)
    # pyautogui.moveTo(300, 300)
    # 마우스 왼쪽 버튼 클릭 해제 (왼쪽 버튼 안 누른 상태)
    # pyautogui.mouseUp()

    pyperclip.copy("서울 날씨") 
    pyautogui.hotkey("ctrl", "v")   # 여러 키를 동시에 입력해야 할 때 hotkey 함수를 쓴다
    time.sleep(0.5)

    pyautogui.write(["enter"]) 
    time.sleep(1)
    
    pyautogui.moveTo(1964,694,0.2)  # (x, y)좌표로 0.2초동안 움직인다
    pyautogui.drag(193,0, duration=0.5) # duration = 이동시간
    # pyautogui.dragTo(1964, 694, duration=0.25)
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.1)
    a = pyperclip.paste()
    # 파이썬에서 copy한 내용을 메모장이나 크롬같은 다른 프로그램에서 붙여넣기 할 수 있고
    # 반대로 다른 프로그램에서 클립보드에 복사한 내용을 파이썬에서 붙여넣기 할 수 있다.
    
    pyautogui.moveTo(464,1105,0.2)
    pyautogui.click()
    time.sleep(0.5)
    pyperclip.copy('#'+a)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    break
#현재 온도24.9°#현재 온도24.9°#현재 온도21.4°