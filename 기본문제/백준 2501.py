"""

아이디어
- N이 주어지면 N번까지 나눈다음 나머지가 0인걸 리스트에 추가.
- index k-1 를 꺼내면된당.
"""

import sys

input = sys.stdin.readline

N, K = map(int,input().split())

i = 1
p = []

while i <= N:
    if N % i == 0:
        p.append(i)
    i += 1

if len(p) < K:
    print(0) #K번째로 작은 약수가 없는 경우.
else:
    print(p[K-1])


