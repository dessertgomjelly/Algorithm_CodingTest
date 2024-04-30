import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
students = deque(map(int, input().split()))
stack = []
number = 1

while number <= n:
    if students and number == students[0]:
        number += 1
        students.popleft()
    elif stack and number == stack[-1]:
        number += 1
        stack.pop()
    else:
        if not students:
            break
        else:
            temp = students.popleft()
            stack.append(temp)

if number > n:
    print('Nice')
else:
    print('Sad')
