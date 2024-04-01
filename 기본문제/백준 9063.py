import sys

input = sys.stdin.readline

N = int(input())
px = []
py = []


for i in range(N):
    x, y = map(int,input().split())
    px.append(x)
    py.append(y)

print((max(px)-min(px)) * (max(py)-min(py)))