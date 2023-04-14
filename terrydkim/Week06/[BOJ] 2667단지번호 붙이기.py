import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().strip())) for i in range(N)]

visited = [[0]*N for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 밖에서 bfs 돌려서 들어갈 때마다 cnt +1 , 안에서 큐에 넣을때마다 count 세고 return count하고 lst에 넣기


def bfs(x, y):
    count = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q :
        a,b = q.pop()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    count += 1
                    q.append((nx,ny))
    return count

cnt = 0
lst = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0 :
            lst.append(bfs(i,j))
            cnt +=1
lst.sort()
print(cnt,*lst,sep='\n')
