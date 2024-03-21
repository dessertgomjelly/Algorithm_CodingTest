"""
대소문자와 공백으로 이루어진 문자열
이문자열에는 단어가 몇개있울까?
"""
"""
아이디어
- 공백구분.
"""

"""
왜 이 코드가 틀렸는지 의문임..
import sys

input = sys.stdin.readline

S = input().strip()
cnt = 0

for i in range(len(S)):
    if S[i] == ' ':
        cnt += 1

print(cnt + 1)
"""
import sys

input = sys.stdin.readline

S = list(map(str,input().split()))

print(len(S))

