import socket                                           # 연결 접속정보 모듈

in_addr = socket.gethostbyname(socket.gethostname())    # 내부 IP

print(in_addr)
