import socket                                 # 연결 접속정보 모듈

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))    # http의 기본 접속 포트는 443

print(in_addr.getsockname()[0])               # 연결된 소켓 이름 출력