import sys

input = sys.stdin.readline

N,X = map(int, input().split())
p = list(map(int,input().split()))

rs = []

for i in range(N):
    if p[i] < X:
        rs.append(p[i])

print(*rs)