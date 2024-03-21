"""x대학 M교수님은 프로그래밍 수업
교실에 30명, 학생 명부엔 각학생별로 1~30
특별과제 28명제출
제출안한사람 2명 출석번호.

제출하지않은 사람중에 출석번호 가장 작은것,
그 다음 출석번호

아이디어
for i+1 in range(28):
1차원 배열 28개를 0으로 초기화 시킨다음에
인덱스랑 매칭 시킨후,

값이 0 인 인덱스 추출.
"""
import sys

input = sys.stdin.readline

p = [0] * 30

for i in range(28):
    x = int(input())
    p[x - 1] = x

for i in range(28):
    if p[i] == 0:
        print(i+1)
