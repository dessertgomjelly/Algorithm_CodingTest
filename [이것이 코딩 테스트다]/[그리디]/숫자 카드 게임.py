"""
행에서 가장 낮은 숫자, 열에서 가장 큰 숫자.
행을 for문돌려서 가장 낮은 숫자를 저장한 뒤. 그중에서 가장 큰 숫자를 뽑으면됨.
"""

import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())

num = [list(map(int,input().split())) for _ in range(N)]
rs = deque()

for i in range(N):
    rs.append(min(num[i]))

print(max(rs))

"""
rsult = 0

for i in range(n):
data = list(map(int,input().split())
min_value = min(data)
result = max(result,min_value)

print(result)
"""