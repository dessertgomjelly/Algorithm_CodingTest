"""
1/1 (0,0)
1/2 (1,0)
2/1 (0,1)
3/1 (0,2)
2/2 (1,1)
1/3 (2,0)
1/4 (3,0)
2/3 (2,1)
3/2 (1,2)
    (0,3)
    (0,4)
    (1,3)


1/1 1번째
1/2 2/1  (+1 -1) 2번째
3/1 2/2 1/3 (-1 +1) 3번째
1/5 2/3 3/2 4/1 (+1 -1) 4번째
5/1 4/2 3/3 2/4 1/5 (-1 +1)

"""
import sys
input = sys.stdin.readline

N = int(input())
line = 1

while N > line:
    N -= line
    line += 1

if line % 2 == 0:
    a = N
    b = line-N+1
else:
    a = line-N+1
    b = N

print(a,"/",b, sep="")




