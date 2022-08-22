'''
itertools
# 하나의 리스트에서 모든 조합을 계산을 해야 한다면 permutations, combinations을 사용
# 두개 이상의 리스트에서 모든 조합을 계산해야 한다면 product를 사용
# 
# Infinite Iterators
# count(start, step)
# cycle(iterable)
# repeat(value, num)
# 
# Combinatoric iterators
# from itertools import product
# from itertools import permutations
# from itertools import combinations

# Terminating iterators
# accumulate(iter, func)
# chain(iter1, iter2)
# islice(iterable, start, stop, step)
'''
import itertools   # 복잡한 반복자를 생성, 리스트의 모든 조합 라이브러리

# 경우의 수를 문자열로 바인딩
passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 1~3까지 반복
for len in range(1,4):
    # 문자열 전부를 1~3까지 반복 튜플로 반환
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)   # 리스트 합치기
        print(passwd)