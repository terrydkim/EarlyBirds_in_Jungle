import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]
matrix = [[0]*n for i in range(n)]
# print(matrix)
x,y = 0,0
idx = 0
for i in range((n*n),0,-1):
    matrix[x][y] = i
    if i == m :
        k,l = x,y
    x = x + dx[idx%4]
    y = y + dy[idx%4]
    if x == n:
        x -= 1
        y += 1
        idx += 1
        continue
    if y == n:
        y -= 1
        x -= 1
        idx += 1
        continue
    if matrix[x][y] != 0:
        x = x - dx[idx%4]
        y = y - dy[idx%4]
        idx += 1
        x = x + dx[idx%4]
        y = y + dy[idx%4]

for j in range(n):
    print(*matrix[j])
print(k+1,l+1)







