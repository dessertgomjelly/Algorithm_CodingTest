import sys

input = sys.stdin.readline

S = input().strip()
dict = ['c=','c-','d-','lj','nj','s=','dz=','z=']
chk = ''
i = 0
cnt = 0

while i < len(S):
    if S[i:i+3] in dict: #예외 조건 dz= 3글자 확인한다음 ex)0:3 0,1,2 니깐 , dz=을 검출되면, 인덱스 3칸 옮기기.
        cnt += 1
        i = i + 3
    elif S[i:i+2] in dict: #2글자 확인 인덱스 2칸 옮기기
        cnt += 1
        i = i + 2
    else:
        cnt += 1 #1글자 옮기기.
        i = i + 1

print(cnt)











