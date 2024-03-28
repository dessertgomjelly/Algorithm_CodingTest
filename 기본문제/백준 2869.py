"""
달팽이문제

낮 A떨어짐
밤 B떨어짐
V미터 올라가기.
며칠 걸리냐.

2 - 1 2 - 1 2 -1

total = 0
while total > V:
cnt =+ 1
total =+ (A - B)

print(cnt)

10억개인데 0.25초 40000만.즉 while, for 는 안댐.
"""



import sys
import math
input = sys.stdin.readline

A, B, V = map(int,input().split())

# 첫째날. A만큼 올라가기때문에 V-B 만큼 더 올라가야함.
# 올라가야할 거리는 V-B, 하루에 갈수 있는 거리는 A-B

day = (V-B) / (A-B)
print(math.ceil(day))