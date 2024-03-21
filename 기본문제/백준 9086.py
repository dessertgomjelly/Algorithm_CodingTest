"""
문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자 출력
문자열을 배열 사용해야할듯?
"""

import sys
input = sys.stdin.readline

x = int(input())

for i in range(x):
    a = str(input().strip())
    print(a[0]+a[-1])