import sys
from collections import deque

stack = deque()
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    S = input().strip()
    for chk in S:
        if chk == '(':
            stack.append(chk)
        elif chk == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
    stack.clear()
