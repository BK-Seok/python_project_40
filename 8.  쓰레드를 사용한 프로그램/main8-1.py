'''
# 파이썬 프로그램은 기본적으로 하나의 쓰레드(Single Thread)에서 실행된다
# 코드를 병렬로 실행하기 위해서는 별도의 쓰레드(Subthread)를 생성해야 함
# 서브쓰레드는 함수 혹은 메서드를 실행
# 쓰레드가 실행할 함수 혹은 메서드를 작성하거나
# 또는 threading.Thread 로부터 파생된 파생클래스를 작성하여 사용
'''
import threading
import time     # 내장 모듈은 주로 epoch time(Unix time, POSIX time)을 다룰 때 사용


def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)
        
# threading 모듈의 threading.Thread() 함수를 호출하여
# Thread 객체를 얻은 후 Thread 객체의 start() 메서드를 호출
t1 = threading.Thread(target=thread_1)
t1.start()  # 바인딩된 t1 실행

while True:
    print("메인동작")
    time.sleep(3.0)
    # time 모듈에 있는 sleep함수, time.sleep(float 초)
    # 초단위로 입력한 시간만큼 프로그램 일시정지
    # time() 함수는 현재 Unix timestamp을 소수로 리턴
    # 정수부는 초단위이고, 소수부는 마이크로(micro) 초단위