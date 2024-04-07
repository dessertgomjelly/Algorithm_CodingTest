"""
1을 찾아나가는 것을 BFS
2중 for문을 돌면서 1이 나올때마다 BFS,(값이 1, 방문 x)일때.
그림개수, 최댓값.

아이디어
- 2중for => 값이 1 && 방문 x => BFS
- BFS돌면서 그림 개수 +1, 최댓값을 갱신

시간복잡도
-BFS : v + E
V = M * N
E = V * 4
O(V+E) = 5V = 250000 < 2억

자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool p[
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy =  [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: #넘어가지 않는 상태
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs


cnt = 0 #전체 그림 개수
maxv = 0 #최대 크기.

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            #전체 그림 개수를 +1
            #BFS 를 통해서 그림의 크기를 구해주고
            maxv = max(maxv, bfs(j,i))
            #최댓값 갱신.

print(cnt)
print(maxv)
