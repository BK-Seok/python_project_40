import sys 
from PyQt5.QtWidgets import *
# pyqt : 기본설치 되어있음
# 파이썬 플러그인으로 구현된
# 크로스 플랫폼 GUI 툴킷 Qt의 파이썬 바인딩
from PyQt5 import uic


ui_path = r"33. 계산기 만들기(PYQT)\계산기.ui"
form_class = uic.loadUiType(ui_path)[0] # ????
# ui 바인딩

# GUI를 구성하는 클래스 상속
class WindowClass(QMainWindow, form_class) : 
    def __init__(self):
        super().__init__()
        # 클래스 초기화
        # 다른 클래스의 속성 및 메소드를 자동으로 불러와
        # 해당 클래스에서도 사용이 가능하도록 해준다
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 인자값을 인스턴스로 받아오는 동작의 객체
    myWindow = WindowClass()
    # GUI를 구성하는 클래스
    myWindow.show()
    # GUI 클래스 출력
    app.exec_()
    # input 객체 실행