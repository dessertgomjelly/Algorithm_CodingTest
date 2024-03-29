"""
주어진 N개 중에서 소수가 몇개인지 찾는 프로그램.

소수가 약수가 없게 소수.

아이디어
- N은 1000이하의 자연수.
- 리스트에 입력받기
- 소수 판별 알고리즘
-
"""

import sys

input = sys.stdin.readline

N = int(input())

num = list(map(int,input().split()))
result = []


for i in range(N):
    a = num[i]
    i = 2
    while i < a:
        if a % i == 0:
            break
        i += 1
    else:
        if a != 1:
            result.append(a)

print(len(result))




