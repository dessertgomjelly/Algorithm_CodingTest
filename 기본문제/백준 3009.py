"""

"""
import sys

input = sys.stdin.readline

px = []
py = []

for i in range(3):
    x, y = map(int, input().strip().split())
    px.append(x)
    py.append(y)

result_px = []
result_py = []

for a in px:
    if px.count(a) == 1:
        result_px.append(a)

for a in py:
    if py.count(a) == 1:
        result_py.append(a)

print(*result_px, *result_py)

