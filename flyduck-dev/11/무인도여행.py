import sys
sys.setrecursionlimit(10**6)

visited = []
answer = []
ans = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

maps_len = 0
def dfs(x,y,arr):
    global maps_len
    global answer
    global ans
    
    ans += int(arr[x][y])
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <maps_len and 0 <= ny <len(arr[0]) and visited[nx][ny] == 0 and arr[nx][ny] != 'X':
            dfs(nx, ny,arr)

def solution(maps):
    global visited
    global answer
    global ans
    global maps_len
    
    maps_len = len(maps)
    visited = [[0]*len(maps[0]) for _ in range(maps_len)]
    arr = []
    for s in maps:
        arr.append([k for k in s])
    
    for u in range(len(arr)):
        for h in range(len(arr[0])):
            ans = 0
            if arr[u][h] != 'X' and visited[u][h] == 0:
                dfs(u,h,arr)
                if ans !=0:
                    answer.append(ans)
                
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer