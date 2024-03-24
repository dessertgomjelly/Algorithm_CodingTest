import sys

input = sys.stdin.readline

p = [list(input().strip()) for _ in range(5)]

# 리스트 하나에 세로부터 저장하면 되겠네 -> 범위초과 그냥 문자열로 해도됨.

rs = ''

for i in range(15):
    for j in range(5):
        if i < len(p[j]):
            print(p[j][i], end = '')




