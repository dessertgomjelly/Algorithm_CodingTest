"""
N개의 시험장, i번 시험장에 있는 응시자의 수는 Ai명.

감독(총감독, 부감독)
총감독은 B명, 부감독은 C명. 부감독은 여러명 가능.
필요한 감독관의 최솟값.

입력
시험장 개수.
각 시험장 응시자수.
B와 C

아이디어
총감독 BB, 부감독 CC이라할때.
- 필요한 감독관은 i*N - (B + C * CC) < 0

"""

import sys

input = sys.stdin.readline

N = int(input()) #시험장
a = list(map(int,input().split())) #각 시험장 응시자수
B, C = map(int, input().split()) #B는 총감독 확인, C는 부감독 확인.
total = 0 # 감독의 수

for i in range(N):
    a[i] = a[i] - B
    total = total + 1
    if a[i] > 0:
        if a[i] % C == 0:
            total = total + (a[i]//C)

        else:
            total = total + (a[i]//C) +1

print(total)
