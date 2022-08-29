import pyautogui
import time
import pyperclip

날씨 = ["서울 날씨","시흥 날씨","청주 날씨","부산 날씨","강원도 날씨"]

addr_x = 1500
addr_y = 90
start_x = 1350
start_y = 400
end_x = 2300
end_y = 980

for 지역날씨 in 날씨:    # 날씨에 바인딩된 인사 수만큼 반복
    pyautogui.moveTo(addr_x,addr_y,1) # 화면기준 이동
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com",interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(지역날씨) # 날씨 인자 문자열 복사
    pyautogui.hotkey("ctrl", "v")    # 붙여넣기
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    저장경로 = '10. 오토마우스를 활용한 웹페이지 자동화\\' + 지역날씨 + '.png'
    pyautogui.screenshot(저장경로, region=(start_x, start_y, end_x-start_x, end_y-start_y))
