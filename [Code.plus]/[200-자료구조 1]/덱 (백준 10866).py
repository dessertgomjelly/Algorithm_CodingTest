import sys
from collections import deque

deque = deque()
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x = input().split()
    if x[0] == 'push_front':
        deque.appendleft(x[1])

    elif x[0] == 'push_back':
        deque.append(x[1])

    elif x[0] =='pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)

    elif x[0] =='pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)

    elif x[0] =='size':
        print(len(deque))

    elif x[0] =='empty':
        if deque:
            print(0)
        else:
            print(1)

    elif x[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)

    elif x[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)