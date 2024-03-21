import sys

input = sys.stdin.readline

p = [0] * 10
cnt = 0


for i in range(10):
    p[i] = int(input())
    p[i] = p[i] % 42

result = set(p)
print(len(result))

