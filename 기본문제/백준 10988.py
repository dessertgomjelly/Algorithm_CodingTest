
import sys

input = sys.stdin.readline

S = list(map(str,input().strip()))

a = len(S)
b = True

for i in range(a//2):
    if S[i] != S[a-i-1]:
        b = False
        break

if b == True:
    print(1)
else:
    print(0)


