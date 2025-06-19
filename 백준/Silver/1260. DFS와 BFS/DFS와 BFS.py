import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
# N:정점 (Node)(Vertex)
# M:간선 (Edge)
# V:시작점

# 2차월 배열 형태 말고 그래프 형태는 어떻게...

graph_bfs = [[] for i in range(N+1)] # 1번 노드부터 저장하려고 N+1

for _ in range(M):
    start, end = map(int, input().split())
    graph_bfs[start].append(end)
    graph_bfs[end].append(start)


for i in range(N+1):
    graph_bfs[i].sort()
    

visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)

graph_dfs = graph_bfs


################## BFS ##################
def bfs_search(graph, start, visited):
    queue = deque([start])
    visited[start] = True 
    bfs = []
    while queue:
        v = queue.popleft() 
        bfs.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
    return bfs
  

################## DFS ##################
def dfs_search(graph, v, visited, dfs):

    visited[v] = True
    dfs.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs_search(graph, i, visited, dfs) 
    return dfs          

 
bfs_list = bfs_search(graph_bfs, V, visited_bfs)  
dfs_list = dfs_search(graph_dfs, V, visited_dfs, [])

print(' '.join(map(str, dfs_list)))
print(' '.join(map(str, bfs_list)))

