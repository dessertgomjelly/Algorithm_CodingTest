import sys
from collections import deque

input = sys.stdin.readline

que = deque()

N = int(input())

for _ in range(N):
    x = input().split()
    if x[0] == 'push':
        que.append(x[1])

    elif x[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif x[0] == 'size':
        print(len(que))

    elif x[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)

    elif x[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)

    elif x[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
