"""
한변의 측면에서 볼때...

초기 : 2
1번 : 3 2+(2-1)
2번 : 5 3+(3-1)
3번 : 9 5+(5-1)
4번 : 17 9+(9-1)

"""

import sys

input = sys.stdin.readline

N = int(input())


width = 3;
p = [0] * N


for i in range(N):
    p[i] = width * width
    width = width + (width - 1)


print(p[-1])
