import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
#N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K
N, M, K = map(int, input().split())
arr = [[0] * (M+1) for i in range(N+1)]
for i in range(K):
    a, b = map(int, input().split())
    arr[a][b] = 1
visited = [[0 for j in range(M+1)] for i in range(N+1)]
# visited와 입력값을 2차원 배열로 만들어서 표시

dy=[0,1,0,-1]
dx=[1,0,-1,0]

#상하좌우 재귀 dfs인 경우 cnt = cnt + 1
def dfs(x,y):
    global cnt
    visited[x][y] = 1
    cnt = cnt + 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N+1 and 0 <= ny < M+1:
            if visited[nx][ny]==0 and arr[nx][ny] == 1:
                dfs(nx, ny)

#[[0, 0, 0, 0, 0],
# [0, 1, 0, 0, 0],
# [0, 0, 1, 1, 0],
# [0, 1, 1, 0, 0]]

cnt_list = []

#이중포문으로 모든 경우 탐색
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 1 and visited[i][j]==0:
            cnt = 0
            dfs(i,j)
            cnt_list.append(cnt)

#이중 포문에서 dfs 불릴 때마다 cnt 값을 갱신 
print(max(cnt_list))