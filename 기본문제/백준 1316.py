"""
아이디어
- 그룹단어의 핵심. 이전단어와 달라야함.
aaaba
"""
import sys

input = sys.stdin.readline

N = int(input())
p = [0] * N

cnt = 0  # 그룹 단어의 개수를 세기 위한 변수

for i in range(N):
    p[i] = input().strip()

for word in p:
    store = []  # 이전에 나온 문자들을 저장하는 리스트
    group_word = True  # 현재 단어가 그룹 단어인지 여부를 저장하는 변수
    prev_char = ''  # 이전 문자를 저장하는 변수

    for char in word:
        if char in store and char != prev_char:
            group_word = False
            break
        else:
            group_word = True
        store.append(char)  # 이전에 나온 문자들을 저장
        prev_char = char  # 이전 문자를 갱신

    if group_word == True:  # 현재 단어가 그룹 단어라면
        cnt += 1  # 그룹 단어의 개수를 1 증가시킴

print(cnt)



"""

저장소 0
- 직전문자 0 = 낫그룹단어
- 직전문자 x = 그룹단어

저장소 x
- 직전문자 상관없이 그룹단어
"""



