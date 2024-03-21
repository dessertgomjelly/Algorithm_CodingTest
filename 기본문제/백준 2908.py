"""
아이디어
-숫자를 뒤집는다. 숫자가 3자리수이다. 0포함 x
-숫자 비교ㄴㄴ 제약조건만으니깐 그냥 그대로 출력
"""

import sys

input = sys.stdin.readline

A,B = input().split()

ar = int(A[2]+A[1]+A[0])
br = int(B[2]+B[1]+B[0])

print(max(ar,br))
