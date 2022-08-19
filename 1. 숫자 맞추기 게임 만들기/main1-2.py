# 임의의 숫자 생성 코드 만들기
import random  # random 함수를 사용하기 위해 random 모듈 불러오기

random_number = random.randint(1, 100)  # 1 ~ 100까지의 수를 변수와 바인딩

# print(random_number)                     # 변수 출력

game_count = 1

while True:
    my_number = int(input("1~100 사이의 숫자를 입력하세요:"))

    if my_number > random_number:
        print("다운")
    elif my_number < random_number:
        print("업")
    elif my_number == random_number:
        print(f"축하합니다.{game_count}회 만에 맞췄습니다.")
        break

    game_count = game_count + 1