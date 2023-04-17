from collections import deque


def bfs(r,c):

    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    q = deque()
  
    q.append((r,c))
    days = int(graph[r][c])
    graph[r][c] = 'X'
              

    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < R and 0 <= nc < C and graph[nr][nc] != 'X':
                
                days += int(graph[nr][nc])
                graph[nr][nc] = 'X'
                q.append((nr, nc))
                
    return days



def solution(maps):
    
    global graph
    global R, C

    graph = [list(row) for row in maps]
    R = len(graph)
    C = len(graph[0])

    answer = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 'X':
                answer.append(bfs(i,j))
    
    answer.sort()
    if answer:
        return answer
    else :
        return [-1]

# print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
# print(solution(["XXX","XXX","XXX"]))











