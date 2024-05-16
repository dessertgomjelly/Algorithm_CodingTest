from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
rs = deque()

for _ in range(N):
    Order = list(input().split())
    if Order[0] == 'push':
        rs.append(Order[1])

    elif Order[0] == 'pop':
        if len(rs) == 0:
            print(-1)
        else:
            print(rs.pop())

    elif Order[0] == 'size':
        print(len(rs))

    elif Order[0] == 'empty':
        if len(rs) == 0:
            print(1)
        else:
            print(0)

    elif Order[0]=='top':
        if len(rs) == 0:
            print(-1)
        else:
            print(rs[-1])

