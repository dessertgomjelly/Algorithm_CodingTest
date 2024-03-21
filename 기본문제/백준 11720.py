"""
N개의 숫자가 공백 없이 쓰여있다.
이 숫자를 모두 합해서 출력하는 프로그램.

아이디어
- 공백없이 쓰여져있다? 문자열로 받는다.
- for문을 돌면서 문자열의 모든 항목 더한다.

자료구조
- 문자열

시간복잡도
-N
"""

import sys

input = sys.stdin.readline

N = int(input())
S = input().strip()

rs = 0

for i in range(N):
    rs += int(S[i]) #문자열을 인트로바꿔줌.

print(rs)