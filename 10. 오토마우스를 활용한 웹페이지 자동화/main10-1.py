import pyautogui    # gui(디스플레이 환경을 자동으로 제어하기 위해 사용)
import time

while True:
    print(pyautogui.position()) # 마우스의 좌표값을 출력
    time.sleep(0.1) # sec(초) 동안 프로그램이 아무것도 하지않고 멈추게함

# 터틀모듈의 position()함수
# import turtle as t
# >>> position = (3.14, -5, 7.5)
# >>> x, y, z = position
# >>> print(x)
# 3.1