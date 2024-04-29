import sys

input = sys.stdin.readline

N, M = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

A_B = set()
B_A = set()

for i in A:
    if i not in B:
        A_B.add(i)

for j in B:
    if j not in A:
        B_A.add(j)

print(len(A_B)+len(B_A))