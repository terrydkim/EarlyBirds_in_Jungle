import sys
input = sys.stdin.readline

#최대이익
# dp    
N = int(input())
lst = [list(map(int,input().split())) for i in range(N)]
dp = [0]*(N+1)

# d[i] = i일이 끝났을 때 얻는 가치
for i in range(N):
    T = lst[i][0]
    P = lst[i][1]
    # 7일까지라 N+1
    for j in range(i+T,N+1):
        if dp[j] < dp[i]+P:
            dp[j] = dp[i]+P
            
print(dp[N])
