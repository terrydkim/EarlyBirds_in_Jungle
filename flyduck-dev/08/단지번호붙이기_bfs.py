import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
visited = [[0]*N for i in range(N)]
for i in range(N):
    arr.append(list(map(int, input().strip())))

dy = [0,1,0,-1]
dx = [1,0,-1,0]
answer = []

def bfs(i,j):
    cnt = 1
    q = deque()
    q.append((i,j)) 
    visited[i][j] = 1
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0<= ny < N:
                if arr[nx][ny] == 1 and visited[nx][ny]==0:
                    q.append([nx,ny])
                    cnt += 1
                    visited[nx][ny] = 1
    return cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            answer.append(bfs(i,j)) 

answer.sort()
print(len(answer))
for home in answer:
    print(home)