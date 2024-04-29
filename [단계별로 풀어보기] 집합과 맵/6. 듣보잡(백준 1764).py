import sys

input = sys.stdin.readline

N, M = map(int, input().split())

listen = set()
see = set()
result = []

for _ in range(N):
    x = input().strip()
    listen.add(x)

for _ in range(M):
    y = input().strip()
    see.add(y)

for i in listen:
    if i in see:
        result.append(i)

result.sort()
print(len(result))

for name in result:
    print(name)
