"""
1~N까지
가장 왼쪽 바구니 첫번째

M번 바구니의 순서를 역순으로 -> 역순으로 바꿀때 순서를 역순으로 만들 범위, 범위에 있는걸 역순
가장 왼쪽 바구니부터 출력.

입력 N,M

아이디어
- 1차원 배열로 바구니에 해당하는 index 에 매핑
- 범위 2중for문으로 매핑

자료구조
배열

시간복잡도
- O(N^2) 100000 < 1억
"""

import sys

input = sys.stdin.readline

N,M = map(int, input().split())

p = [0] * N

for i in range(N):
    p[i] = i+1

for i in range(M):
    x, y = map(int,input().split())
    for j in range((y-x + 1) // 2):
        temp = p[x + j - 1]
        p[x + j - 1] = p[y - j -1]
        p[y - j - 1] = temp

print(*p)



"""
x
1~5/2
4/2 
print(*p)

(y-x + 1) / 2


p[0] =1
p[1] = 2
p[2] = 3
p[3] = 4
p[4] = 5
...
p(N-1) = N

!! 아이디어
왼쪽꺼는 x 부터 1씩 증가 -> 오른쪽은 y부터 1씩 감소
근데 인덱스 매핑 해줘야하기때문에 -1 추가.

"""