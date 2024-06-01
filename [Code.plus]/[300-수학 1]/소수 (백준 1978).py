import math

n = int(input())

num = list(map(int, input().split()))

def primenumber(x):
    if x < 2:
        return False
    for i in range (2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

chk = 0
for x in num:
    if primenumber(x):
        chk += 1

print(chk)



