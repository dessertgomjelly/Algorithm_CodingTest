import sys

input = sys.stdin.readline

N = int(input())

info = []

for _ in range(N):
    i,j = input().split()
    info.append((int(i),j))


result = sorted(info, key = lambda x : x[0])

for i in result:
    print(i[0], i[1])

"""
import sys

input = sys.stdin.readline

N = int(input())

info = []

# 회원 정보 입력 받기
for idx in range(N):
    age, name = input().split()
    info.append((int(age), name, idx))  # 인덱스 정보 추가

# 나이와 인덱스를 기준으로 정렬
info.sort(key=lambda x: (x[0], x[2]))

# 정렬된 회원 정보 출력
for i in info:
    print(i[0], i[1])
"""