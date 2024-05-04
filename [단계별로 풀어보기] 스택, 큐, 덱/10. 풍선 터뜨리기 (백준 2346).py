import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque([])

order = list(map(int, input().split()))

for idx, o in enumerate(order):
    q.append((o, idx+1))

rs = []

while q:
    a = q.popleft()
    print(a[1],end=' ')
    if a[0] < 0:
        q.rotate(-a[0])
    else:
        q.rotate(-a[0]+1)

