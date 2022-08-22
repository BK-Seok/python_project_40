import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 경로
zFile = zipfile.ZipFile(r'6. 압축파일 암호 푸는 프로그램\암호123.zip')

for len in range(1,5):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            # extractall 메서드로 모든파일 압축 해제
            zFile.extractall(pwd = passwd.encode())
            print (f"비밀번호는 {passwd} 입니다")
            break
        except:
            pass