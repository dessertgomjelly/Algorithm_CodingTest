import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    for i in range(max(A, B), (A*B)+1):
        if i % A == 0 and i % B == 0:
            print(i)
