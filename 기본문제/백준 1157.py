import sys

input = sys.stdin.readline

# 먼저, 대문자로 바꿈
p = input().strip()
P = p.upper()
dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #딕셔너리 선언
cnt = [0]*len(dict) #알파벳만큼의 리스트 만들기

for i in P: #P문자열을 하나하나 살펴보면서
    if i in dict: #딕셔너리에 값이 같은게 있다면
        index = dict.index(i) # 해당 알파벳이 몇번째인지 알아내고
        cnt[index] += 1 #알파벳 카운트 리스트에 개수 추가.

y = max(cnt) #최댓값

if cnt.count(y) > 1: #최댓값이 1개 이상이면
    print("?") # ? 출력
else:
    print(dict[cnt.index(y)]) #아니면 최댓값 인덱스를 딕셔너리에 매핑시키기



