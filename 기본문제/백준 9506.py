"""
아이디어
-어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면 완전수.
-
- 입력의 마지막에 -1, 즉 while문을 사용해라.
"""

import sys

input = sys.stdin.readline


while True:
    N = int(input())
    if N == -1:
        break
    i = 1
    p = []
    while i < N:
        if N % i == 0:
            p.append(i)
        i += 1

    if sum(p) == N:
        print(N, "=", " + ".join(map(str,p)))
    else:
        print(N,"is NOT perfect.")



