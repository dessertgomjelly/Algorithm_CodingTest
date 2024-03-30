"""
한수는 (x,y)에 있다.
직사각형은 각변이 좌표축에 평행. 꼭짓점 (0,0) 오른쪽 위 꼭짓점은 (w,h)
"""

import sys
import math
input = sys.stdin.readline

x, y, w, h = map(int,input().split())

print(min(x, y, w-x, h-y))