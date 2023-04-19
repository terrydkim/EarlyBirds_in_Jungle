# 스티커 오답 
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    arr =[]
    for i in range(2):
        info = list(map(int, input().split()))
        arr.append(info)
    dp = [[0]* n for j in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[0][i-2], arr[0][i] + dp[1][i-1])
        dp[1][i] = max(dp[1][i-2], arr[1][i] + dp[0][i-1])

    print(max(dp[0][n-1], dp[1][n-1]))