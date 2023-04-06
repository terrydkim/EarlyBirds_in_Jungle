import sys
input = sys.stdin.readline
n = int(input())
board = []
for i in range(n):
    arr = list(map(ord, input().strip()))
    board.append(arr)

last_num = 0
cnt_arr = [] 
cnt = 1
for i in range(n-1):
    last_num == board[i][0]
    for j in range(n-1):
        if board[i][j] == board[i][j+1] and last_num == board[i][j]:
            cnt += 1
            continue
        elif board[i][j] == board[i][j+1] and last_num != board[i][j]:
            cnt_arr.append(cnt)
            cnt = 2      
        else:
            cnt_arr.append(cnt)
            temp = board[i][j]
            board[i][j] = board[i][j+1]
            board[i][j+1] = board[i][j]
            last_num == board[0][j]
            cnt = 1
            for k in range(0, n-1):
                if board[k][j] == board[k+1][j] and last_num == board[k+1][j]:
                    cnt += 1
                else:
                    cnt_arr.append(cnt)
                    cnt = 1
            cnt = 1


print(max(cnt_arr))
