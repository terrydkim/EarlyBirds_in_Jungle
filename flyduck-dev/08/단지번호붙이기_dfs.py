import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = []
visited = [[0]*N for i in range(N)]
for i in range(N):
    arr.append(list(map(int, input().strip())))

dy = [0,1,0,-1]
dx = [1,0,-1,0]
answer = []
cnt = 0 
def dfs(i,j):
    global cnt
    cnt += 1
    visited[i][j] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0<= ny < N:
            if arr[nx][ny] == 1 and visited[nx][ny]==0:
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i,j)
            answer.append(cnt) 

answer.sort()
print(len(answer))
for home in answer:
    print(home)

