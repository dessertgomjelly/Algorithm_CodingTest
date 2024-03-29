"""
M이상 N이하 중 소수를 골라
소수의합.
최솟값.
출력

아이디어
- M부터 N까지. 숫자.
for i in range(M,N+1):
리스트에 저장.

리스트에 하나씩 빼면서 소수찾기 돌려.
- 소수 찾기란 1 제외 하고, 자기 자신만 나눠지는것.

그걸 또 리스트에 저장.
"""

import sys

input = sys.stdin.readline

M = int(input())
N = int(input())

num = []
for i in range(M,N+1):
    num.append(i)

result = []
for i in num:
    a = 2
    while a < i:
        if i % a == 0:
            break
        a += 1
    else:
        if i != 1:
            result.append(a)

if len(result) < 1:
    print(-1)
else:
    print(sum(result))
    print(min(result))

