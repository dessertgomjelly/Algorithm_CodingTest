import sys

input = sys.stdin.readline

N, M = map(int, input().split())

word_set = set()

for _ in range(N):
    a = input().strip()
    word_set.add(a)  # 입력된 단어를 집합에 추가

count = 0

for _ in range(M):
    a = input().strip()
    if a in word_set:
        count += 1

print(count)
