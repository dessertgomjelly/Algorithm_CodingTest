import sys

input = sys.stdin.readline

N = (input().strip())

rs = []

for i in N:
    rs.append(int(i))

rs.sort(reverse=True)

print(*rs,sep="")