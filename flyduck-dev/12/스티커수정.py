# 스티커 수정
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr =[]
    for i in range(2):
        info = list(map(int, input().split()))
        arr.append(info)
    dp = [[0]* n for i in range(2)]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    else:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-2],dp[1][i-1]) + arr[0][i]
            dp[1][i] = max(dp[0][i-2],dp[0][i-1]) + arr[1][i]

        print(max(max(dp[0]), max(dp[1])))