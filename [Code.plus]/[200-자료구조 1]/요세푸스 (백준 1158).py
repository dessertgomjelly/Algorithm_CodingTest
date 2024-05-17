"""
1 2 3 4 5 6 7

두개씩 옮기면서 하나빼고 영구적 삭제.
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
que = deque()
rs = []

for i in range(1,n+1):
    que.append(i)


while len(que) > 0:
    for _ in range(k-1):
        que.append(que.popleft())
    rs.append(que.popleft())

print("<", end="")
for i in rs:
    print(i, end="")
    if i != rs[-1]:
        print(end=", ")
print(">")