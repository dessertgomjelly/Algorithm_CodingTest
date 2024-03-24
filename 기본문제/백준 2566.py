"""
아이디어
- 2차원 배열에다가 입력 받기.
최댓값 받은다음에 비교.

"""
import sys

input = sys.stdin.readline

P = [list(map(int,input().split())) for _ in range(9)]

i = 0
j = 0
store = []
rs = 0

for i in range(9):
    for j in range(9):
        store.append(P[i][j])

print(max(store))
for i in range(9):
    for j in range(9):
        if P[i][j] == max(store):
            print(i+1, j+1)







