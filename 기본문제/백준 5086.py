"""


"""
import sys

input = sys.stdin.readline

#입력 계속 받아야해서 무조건 while문.

while True:
    X, Y = map(int,input().split())
    if X < Y and Y % X == 0:
        print("factor")
    elif X > Y and X % Y == 0:
        print("multiple")
    elif X == 0 and Y == 0:
        break
    else:
        print("neither")
