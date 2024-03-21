"""
아이디어
- 바구니 N개에 미리 0을 넣기
- 이중 for 문
    - (i부터 j까지 K 넣기)를 M번

자료구조
- 1차원 배열

시간복잡도
- M * M = M^2 10000 < 2억
"""

import sys

# input() 대신 sys.stdin.readline()을 사용하여 입력을 받기
input = sys.stdin.readline

N, M = map(int, input().split())

# 바구니 N개에 초기값 0을 넣기
p = [0] * N

# M번 반복하여 작업을 수행합니다.
for _ in range(M):
    i, j, k = map(int, input().split())
    # i부터 j까지의 구간에 k를 넣기
    for idx in range(i-1, j):
        p[idx] = k

# 결과 출력
print(p)
