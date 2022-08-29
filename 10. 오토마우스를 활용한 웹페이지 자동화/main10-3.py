import pyautogui
import time
import pyperclip

pyautogui.moveTo(1700,360,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨") 
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"]) 
time.sleep(1)

start_x = 1350
start_y = 540
end_x = 2300
end_y = 980

pyautogui.screenshot(r'10. 오토마우스를 활용한 웹페이지 자동화\서울날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
