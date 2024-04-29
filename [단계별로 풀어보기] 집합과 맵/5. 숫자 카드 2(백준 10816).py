import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
xx = list(map(int, input().split()))

hash = {}

for num in nums:
    if num in hash:
        hash[num] += 1
    else:
        hash[num] = 1


for x in xx:
    if x in hash:
        print(hash[x],end = ' ')
    else:
        print(0, end = ' ')