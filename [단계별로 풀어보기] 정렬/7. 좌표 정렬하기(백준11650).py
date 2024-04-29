import sys

input = sys.stdin.readline

N = int(input())
Point = []

for _ in range(N):
    i, j = map(int, input().split())
    Point.append((i,j))

Point.sort()

for point in Point:
    print(point[0],point[1])


