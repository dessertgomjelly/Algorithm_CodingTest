import sys

input = sys.stdin.readline

while True:
    p = sorted(list(map(int,input().split())))
    if p[0] == 0 and p[1] == 0 and p[2] == 0:
        break

    if p[0] + p[1] <= p[2]:
        print("Invalid")

    elif p[0] ==asdfdsafdsafadsadsffd