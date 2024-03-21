"""
아이디어
-1차원 배열로 N개만큼 만듦
for문 돌면서 v와 같으면 cnt +1

자료구조
배열

시간복잡도
N
"""

import sys

input = sys.stdin.readline
N = int(input())

p = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(N):
    if p[i] == v:
        cnt += 1


print(cnt)


