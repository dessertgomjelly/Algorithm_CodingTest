import sys

input = sys.stdin.readline

N = int(input())

p = list(map(int,input().split()))

rs = []


rs.append(min(p))
rs.append(max(p))

print(*rs)
