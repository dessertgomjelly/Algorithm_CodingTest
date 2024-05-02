from collections import deque
import sys

input = sys.stdin.readline
x = deque()


N = int(input())

for _ in range(N):
    X = list(map(int, input().split()))
    if X[0] == 1:
        x.appendleft(X[1])

    elif X[0] == 2:
        x.append(X[1])

    elif X[0] == 3:
        if len(x) == 0:
            print(-1)
        else:
            print(x.popleft())

    elif X[0] == 4:
        if len(x) == 0:
            print(-1)
        else:
            print(x.pop())

    elif X[0] == 5:
        print(len(x))

    elif X[0] == 6:
        if len(x) == 0:
            print(1)
        else:
            print(0)

    elif X[0] == 7:
        if len(x) == 0:
            print(-1)
        else:
            print(x[0])

    elif X[0] == 8:
        if len(x) == 0:
            print(-1)
        else:
            print(x[-1])





