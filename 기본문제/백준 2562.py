import sys

input = sys.stdin.readline

p = [0]*10

for i in range(9):
    x = int(input())
    p[i+1] = x

print(max(p))
print(p.index(max(p)))
