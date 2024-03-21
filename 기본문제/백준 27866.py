"""
단어 S와 정수 i가 주여졌을 때, S의 i번째 글자를 출력하는 프로그램.
"""

import sys

input = sys.stdin.readline

S = str(input())

i = int(input())

print(S[i-1])