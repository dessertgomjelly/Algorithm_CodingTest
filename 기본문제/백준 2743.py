"""
알파벳으로만 이루어진 단어를 입력받ㅇ, 그 길이를 출력

"""

import sys
#sys.stdin.readline을 하면 줄바꿈문자포함 \n .strip()
input = sys.stdin.readline

S = str(input().strip())

print(len(S))