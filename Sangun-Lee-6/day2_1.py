import sys
input = sys.stdin.readline
from collections import deque
q = deque()

R, C, K = map(int, input().split())
graph = [[0] * (C) for _ in range(R)]

for _ in range(K):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def bfs(r,c):
    
    graph[r][c] = 0
    q.append((r,c))
    area = 1
    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<=nr<R and 0<=nc<C and graph[nr][nc] == 1:
                graph[nr][nc] = 0
                q.append((nr, nc))
                area +=1
    return area

ans = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] ==1:
            ans = max(bfs(i,j), ans)

print(ans)



