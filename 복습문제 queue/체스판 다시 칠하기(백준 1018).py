import sys

# 입력 처리
input = sys.stdin.readline
N, M = map(int, input().split())

# 보드 생성
board = [list(input().strip()) for _ in range(N)]

# 최소 변경 횟수를 저장할 리스트
repair = []

# 각 8x8 블록에 대해 처리
for i in range(N - 7):
    for j in range(M - 7):
        w_first = 0
        b_first = 0
        # 8x8 블록 탐색
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 짝수 행+열이거나 홀수 행+열일 때 색깔 변경 횟수 계산
                if (x + y) % 2 == 0:  
                    if board[x][y] != 'W':
                        w_first += 1
                    if board[x][y] != 'B':
                        b_first += 1
                else:
                    if board[x][y] != 'W':
                        w_first += 1
                    if board[x][y] != 'B':
                        b_first += 1

        # 최소 변경 횟수 저장
        repair.append(w_first)
        repair.append(b_first)

# 최소 변경 횟수 출력
print(min(repair))

"""
# 8*8 블럭이 될 수 있는 모든 경우의 수에서
# min(res, 블록을 교체해야 하는 횟수)
# 각 원소에서 오른쪽으로 + 7, 아래로 + 7

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

repair = []

for i in range(n-7):
    for j in range(m-7):
        w_first = 0
        b_first = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        w_first += 1
                    if board[k][l] != 'B':
                        b_first += 1
                else:
                    if board[k][l] != 'B':
                        w_first += 1
                    if board[k][l] != 'W':
                        b_first += 1
        repair.append(w_first)
        repair.append(b_first)

print(min(repair))"""