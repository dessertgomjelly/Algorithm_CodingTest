"""
M : 자기점수 최댓값

점수 / M*100

50 / 100 * 100

50점인데?

500/7 =


흠..
아이디어
- 배열에다가 N개의 점수
- 최댓값 max 로 뽑아.
- for문으로 M의 평균 즉 배열 순회 하면서,
- 그걸 출력할때 N으로 나워.
"""

import sys

input = sys.stdin.readline

N = int(input())

p = list(map(int, input().split()))

M = max(p)

rs = [0] * N

for i in range(N):
    rs[i] = p[i] / M
    p[i] = rs[i] * 100

print(sum(p) / N)

