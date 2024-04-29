import sys

input = sys.stdin.readline

N = (input().strip())

rs = []

for i in N:
    rs.append(i)

rs.sort(reverse=True)

print(*rs,sep="")