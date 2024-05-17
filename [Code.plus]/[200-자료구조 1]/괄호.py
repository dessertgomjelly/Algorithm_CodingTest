import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    xx = input().strip()
    st = deque()
    for x in xx:
        if x == '(':
            st.append(x)
        elif x == ')':
            if len(st) != 0:
                st.pop()
            else:
                print('NO')
                break

    else:
        if len(st) == 0:
            print('YES')
        else:
            print('NO')



