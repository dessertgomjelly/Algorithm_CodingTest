import sys

input = sys.stdin.readline

N, M = map(int, input().split())

poket_name = {}
poket_id = {}
for i in range(1,N+1):
    poket = input().strip()
    poket_name[poket] = i
    poket_id[i] = poket

for _ in range(M):
    x = input().strip()
    if x.isdigit():
        x = int(x)
        print(poket_id[x])
    else:
        print(poket_name[x])

