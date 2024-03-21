"""
아이디어
처음 바구니 번호와 같은 공으로 채우기
두 바구니 공 M번 교환,
M번 바꾼 이후 각 바구니에 어떤 공이 있을까.

자료구조
바구니 : 배열 int[]

시간복잡도
바구니 : 배열 N번
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # N은 바구니 개수, M은 몇 번 공을 바꿀지.

p = [[i + 1] for i in range(N)]  # 처음에는 각 바구니에 바구니 번호와 같은 공으로 채움

for _ in range(M):
    i, j = map(int, input().split())
    p[i - 1], p[j - 1] = p[j - 1], p[i - 1]  # 공의 위치를 서로 바꿈

for ball in p:
    print(*ball, end=' ')  # 각 바구니에 들어있는 공의 번호를 공백으로 구분하여 출력
