"""
아이디어
- for 문 돌면서. 세장의 합 최댓값 갱신. 이때 if문으로 조건걸기
"""
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
cards = list(map(int,input().split()))

max_sum = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            cardsum = cards[i] + cards[j] + cards[k]
            if cardsum <= M:
                if cardsum > max_sum:
                    max_sum = cardsum

print(max_sum)

