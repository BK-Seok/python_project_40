import pyautogui
import time
import pyperclip

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
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    pyautogui.write(["enter"]) 
    time.sleep(1)
    
    pyautogui.moveTo(1964,694,0.2)
    pyautogui.drag(193,0, duration=0.5)
    # pyautogui.dragTo(1964, 694, duration=0.25)
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.1)
    a = pyperclip.paste()
    
    pyautogui.moveTo(464,1105,0.2)
    pyautogui.click()
    time.sleep(0.5)
    pyperclip.copy('#'+a)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    break
#현재 온도24.9°#현재 온도24.9°