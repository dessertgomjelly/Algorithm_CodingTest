import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 보드의 크기
K = int(input())  # 사과 개수
apples = [list(map(int, input().split())) for _ in range(K)]  # 사과 좌표
L = int(input())  # 변환 횟수
turns = [input().split() for _ in range(L)]  # X는 변환시간, C는 방향전환

# 보드 생성 및 사과 표시
board = [[0] * N for _ in range(N)]

for y, x in apples:
    board[y - 1][x - 1] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 뱀의 초기 위치 및 방향 설정
x, y, d = 0, 0, 0
snake = deque([(y, x)])
time = 0
time_dic = {}

# 방향 전환 정보 저장
for t, c in turns:
    time_dic[int(t)] = c

while True:
    time += 1

    # 다음 위치 계산
    x += dx[d]
    y += dy[d]

    # 벽 또는 자기 몸에 부딪히면 게임 종료
    if not (0 <= y < N and 0 <= x < N) or (y, x) in snake:
        break

    # 사과가 있는 경우
    if board[y][x] == 1:
        board[y][x] = 0  # 사과 먹기
    else:  # 사과가 없는 경우
        snake.popleft()  # 꼬리 이동

    snake.append((y, x))  # 뱀의 머리 이동

    # 시간에 따라 방향 전환
    if time in time_dic:
        if time_dic[time] == 'D':  # 시계 방향으로 90도 회전
            d = (d + 1) % 4
        else:  # 반시계 방향으로 90도 회전
            d = (d - 1) % 4

print(time)
