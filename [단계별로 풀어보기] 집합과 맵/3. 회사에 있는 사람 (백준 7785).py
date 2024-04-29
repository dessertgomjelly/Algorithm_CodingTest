"""
직원들은 원할때 출근 아무때나 퇴근
로그 출입기록
현재 회사에 있는 모든 사람.
enter 를하고 leave가 없는 사람 구하기문제.

"""

import sys

input = sys.stdin.readline

n = int(input())

chk = {}

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        chk[name] = True
    else:
        del chk[name]

result = sorted(chk.keys(), reverse=True)
for rs in result:
    print(rs)
