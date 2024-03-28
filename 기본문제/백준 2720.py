"""
동혁이 거스름돈

쿼터 = 0.25
다임 = 0.10
니켈 = 0.05
페니 = 0.01

그리디알고리즘으로 쿼터로 나눈다음에 나머지를 다음으로 나머지를 니켈로 나머지를 페니로
쿼터 다임 니켈 페니 cnt 하면된다.

자료구조
- 돈 : int
- cnt : int
- cnt 저장 : []
- 전체 돈 : 1차원 배열
"""

import sys

input = sys.stdin.readline

T = int(input().strip())

exchange = list(int(input()) for _ in range(T))


def money(num):
    # 각 동전의 가치
    coins = [0.25, 0.1, 0.05, 0.01]
    # 각 동전의 개수를 저장할 변수 초기화
    counts = [0, 0, 0, 0]
    # 각 동전의 가치와 주어진 금액을 비교하여 최소 동전 개수 계산
    for i in range(len(coins)):
        while num >= coins[i]:
            num -= coins[i]
            counts[i] += 1

    return counts


for num in exchange:
    result = money(num)
    print(result)
"""

import sys

input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스의 개수 T를 입력 받음

for _ in range(T):
    C = int(input().strip())  # 거스름돈 C를 입력 받음

    # 거스름돈을 가장 큰 단위의 동전부터 사용하여 나누기
    quarters = C // 25  # 쿼터의 개수 계산 몫.
    C %= 25  # 나머지를 다음 동전을 계산하기 위해 저장

    dimes = C // 10  # 다임의 개수 계산
    C %= 10

    nickels = C // 5  # 니켈의 개수 계산
    C %= 5

    pennies = C  # 페니의 개수는 남은 센트 그대로

    # 결과 출력
    print(quarters, dimes, nickels, pennies)
    """