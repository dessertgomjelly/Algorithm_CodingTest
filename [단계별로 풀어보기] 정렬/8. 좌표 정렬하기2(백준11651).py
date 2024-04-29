import sys

input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((y, x))

points.sort()

for point in points:
    print(point[1], point[0])
