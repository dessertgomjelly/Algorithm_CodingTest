import sys

input = sys.stdin.readline

p = [0] * 10

for i in range(10):
    p[i] = int(input())
    p[i] = p[i] % 42

unique = []
cnt = 0

for i in p:
    try:
        unique.index(i)
    except ValueError:
        unique.append(i)
        cnt += 1

print(cnt)
