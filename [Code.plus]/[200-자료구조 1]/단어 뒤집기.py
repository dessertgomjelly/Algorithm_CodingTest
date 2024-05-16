import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    words = input().split()
    for word in words:
        rs = word[::-1]
        print(rs, end=" ")
    print()
