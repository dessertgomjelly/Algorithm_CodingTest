import sys

input = sys.stdin.readline

N = int(input())
papers = []
for _ in range(N):
    x, y = map(int, input().split())
    papers.append((x,y))

p = [[0] * 100 for _ in range(100)]

for x,y in papers:
    for i in range(y, y+10):
        for j in range(x, x+10):
            p[i][j] = 1

cnt = 0

for i in range(100):
    for j in range(100):
        if p[i][j] == 1:
            cnt += 1


print(cnt)