"""
자기 자신보다 작으면서 서로달라야함.

"""
import sys

input = sys.stdin.readline

N = int(input())

store = list(map(int, input().split()))

result = sorted(set(store))

dic = {result[i] : i for i in range(len(result))}

for i in store:
    print(dic[i], end = ' ')