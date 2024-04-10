"""
M = N + N의 자릿수.
N이 주어졌을 때 가장 작은 생성자 찾기.
그리디 알고리즘?
일단 리스트로 숫자 각각을 받으면서 그 수가 가장 커야해
근데 가장 작기 위해서는?
"""

import sys
input = sys.stdin.readline

# 입력
n = int(input())

for i in range(n):
    # 분해합 공식
    digit_sum = i + sum(map(int, str(i)))
    # 생성자일 경우
    if digit_sum == n:
        print(i)
        break
else:
    print(0)
