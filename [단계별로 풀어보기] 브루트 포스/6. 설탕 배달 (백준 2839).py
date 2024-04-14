import sys
input = sys.stdin.readline

N = int(input())
bags = 0
while N> 0 :
    if N % 5 == 0:
        bags += N//5
        break
    else:
        N -= 3
        bags += 1

if N < 0:
    print(-1)
else:
    print(bags)
