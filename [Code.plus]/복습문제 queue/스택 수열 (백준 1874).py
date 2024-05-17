import sys

input = sys.stdin.readline
n = int(input())
stack = []
rs = []
current = 1

for i in range(n):
    x = int(input())
    while current <= x:
        stack.append(current)
        rs.append('+')
        current += 1

    if stack[-1] == x:
        stack.pop()
        rs.append('-')
    else:
        print("NO")
        break

else:
    for i in rs:
        print(i)










