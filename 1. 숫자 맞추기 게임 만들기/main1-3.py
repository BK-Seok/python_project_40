# 임의의 숫자 생성 코드 만들기
import random                            # random 함수를 사용하기 위해 random 모듈 불러오기

random_number = random.randint(1, 100)   # 1 ~ 100까지의 임의의 정수를 변수와 바인딩

#print(random_number)                     # 변수 출력

game_count = 1                           # 게임 횟수 카운트 초기 값 바인딩

while True:                              # 무한 반복
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요:")) # 입력값을 정수형태로 변수에 바인딩
                                                            # 문자형은 받을 수 없으며 에러 발생
        if my_number > random_number:        # 입력값과 임의의값을 비교
            print("다운")
        elif my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"축하합니다.{game_count}회 만에 맞췄습니다.") # f-string을 이용해 문자열, 변수 출력
            break

        game_count = game_count + 1          # 실행될때마다 게임 수 1씩 증가
    except:
        print("에러가 발생하였습니다. 숫자를 입력하세요.")