import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


N, M, R = map(int, input().split())

# 그래프와 방문 여부 리스트 초기화
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 간선 입력 및 그래프 생성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
# DFS 실행
def dfs(graph, visited, R):
    visited[R] = True

    for i in graph[R]:
        if not visited[i]:
            dfs(graph, visited, i)

dfs(graph, visited, R)

# 방문한 노드 순서 출력
for i in range(1, N+1):
    if visited[i]:
        print(i)
# 방문하지 못한 노드는 0으로 표시
for i in range(1, N+1):
    if not visited[i]:
        print(0)
