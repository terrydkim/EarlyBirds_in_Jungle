from collections import deque

def solution(maps):
    answer = 0
    q = deque()
    x,y = 0,0
    q.append((x,y))
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    while (q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] += maps[x][y]
                # cnt += 1
    # if cnt == 0 :
        # return -1
    # else:
        # return cnt
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
    
    # if maps[n-1][m-1] == 1:
    #     return -1
    # else:
    #     return maps[n-1][m-1]


# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))