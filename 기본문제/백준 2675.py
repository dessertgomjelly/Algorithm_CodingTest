"""
아이디어 :
for 문 돌려서 인덱스 곱하기 R번 하면되잖아.
"""

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = input().split()
    r = int(R)

    result = ''
    for j in range(len(S)):
        result += S[j] * r


    print(result)


