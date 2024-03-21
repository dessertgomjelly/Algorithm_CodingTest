import sys

input = sys.stdin.readline

S = list(map(str,input().strip())) #이거 불필요한 과정이라네
#s = list(input)으로 하면된다네

r1 = 'ABC'
r2 = 'DEF'
r3 = 'GHI'
r4 = 'JKL'
r5 = 'MNO'
r6 = 'PQRS'
r7 = 'TUV'
r8 = "WXYZ"

time = 0

for i in range(len(S)):
    if S[i] in r1:
        time += 2
    elif S[i] in r2:
        time += 3
    elif S[i] in r3:
        time += 4
    elif S[i] in r4:
        time += 5
    elif S[i] in r5:
        time += 6
    elif S[i] in r6:
        time += 7
    elif S[i] in r7:
        time += 8
    elif S[i] in r8:
        time += 9

print(time+len(S))