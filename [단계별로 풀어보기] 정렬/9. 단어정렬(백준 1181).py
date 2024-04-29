import sys

input = sys.stdin.readline

N = int(input())

words = []
for _ in range(N):
    x = input().strip()
    words.append(x)

words = list(set(words))

words.sort(key = lambda x : (len(x),x))

for word in words:
    print(word)

