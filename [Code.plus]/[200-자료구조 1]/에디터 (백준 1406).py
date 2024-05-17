from collections import deque
import sys

input = sys.stdin.readline

left = deque(input().strip())
right = deque()

n = int(input())
for _ in range(n):
    Order = input().split()
    if Order[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif Order[0] == 'D':
        if right:
            left.append(right.popleft())
    elif Order[0] == 'B':
        if left:
            left.pop()
    elif Order[0] == 'P':
        left.append(Order[1])


print(''.join(left) + ''.join(right))
