"N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오."

"""
import sys

input = sys.stdin.readline

N = int(input())

store = list(int(input()) for _ in range(N))

store.sort()

print(*store, sep = '\n')
메모리 초과
"""
import sys

input = sys.stdin.readline
N = int(input())
arr = [0] *10001 #입력이 10000개 주어짐

for _ in range(N):
    x = int(input())
    arr[x] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)