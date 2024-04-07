from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]
que = deque()
chk = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                ry, rx = i, j
            elif board[i][j] == 'B':
                by, bx = i, j
    que.append((ry, rx, by, bx, 1))
    chk[ry][rx][by][bx] = True  # 구슬이 들렸던 위치 기록


def move(y, x, dy, dx):
    cnt = 0
    while True:  # 이 부분 수정
        if board[y+dy][x+dx] == '#':
            break
        if board[y][x] == 'O':
            break
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def bfs():
    init()
    while que:
        ry, rx, by, bx, cnt = que.popleft()
        if cnt > 10:
            return -1

        for i in range(4):
            nry, nrx, nrc = move(ry, rx, dy[i], dx[i])
            nby, nbx, nbc = move(by, bx, dy[i], dx[i])
            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                return cnt

            if nry == nby and nrx == nbx:
                if nrc > nbc:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]

            if not chk[nry][nrx][nby][nbx]:
                chk[nry][nrx][nby][nbx] = True
                que.append((nry, nrx, nby, nbx, cnt+1))

    return -1

# 함수 호출 및 결과 출력
print(bfs())
