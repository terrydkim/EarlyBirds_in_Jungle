import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, m, k = map(int, input().split())

graph = [[0]*(m+1) for i in range(n+1)]
visited = [[0]*(m+1) for i in range(n+1)]

for i in range(k):
    a,b = map(int,input().split())
    graph[a][b] = 1
# matrix = [list(map(int, input().split())) for i in range(k)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n+1 and 0 <= ny < m+1 :
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx,ny)
                cnt += 1

res = 0
for i in range(n+1):
    for j in range(m+1):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i,j)
            res = max(res,cnt)
print(res)




# def dfs(x, y):
#     global cnt
#     visited[x][y] = 1
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0 <= nx < n and 0 <= ny <m and visited[nx][ny] == 0:
#             dfs(nx,ny)
#             visited[nx][ny] = 0
#             cnt += 1
#     return cnt
# for i,j in matrix:
#     visited[i][j] = 0
# # 하나씩 dfs에 넣기
# for i, j in matrix:
#     max(cnt,dfs(i, j))
# print(cnt)



# def dfs(x,y):
    


# def dfs(x):
#     global cnt
#     visited[x] = 1
#     for i in graph:
#         if not visited[i]:
#             dfs(i)
#             cnt += 1
#     return cnt
# print(dfs(0))