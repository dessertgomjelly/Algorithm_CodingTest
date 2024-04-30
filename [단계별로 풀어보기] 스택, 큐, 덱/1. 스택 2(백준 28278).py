import sys

input = sys.stdin.readline

N = int(input())
ST = []

for _ in range(N):
    a = list(map(int, input().split()))
    if a[0] == 1:
        ST.append(a[1])
    elif a[0] == 2:
        if len(ST) > 0:
            print(ST.pop())
        else:
            print(-1)
    elif a[0] == 3:
        print(len(ST))
    elif a[0] == 4:
        if len(ST) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 5:
        if len(ST) > 0:
            print(ST[-1])
        else:
            print(-1)

