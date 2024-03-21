"""
검정 피스는 모두있지만 흰색 피스는 없다.

킹 1
퀸 1
룩 2
비숍 2
나이트 2
폰 8

아이디어
- 리스트 1 1 2 2 2 8
- 입력 리스트로 만든 다음, 같은 인덱스 빼기 출력
"""
import sys

input = sys.stdin.readline

r = [1,1,2,2,2,8]

p = list(map(int , input().split()))

rs = [0]*6

for i in range(6):
    rs[i] = r[i] - p[i]

print(*rs)
