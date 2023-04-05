import sys
input = sys.stdin.readline

n = int(input())
scehdule = []

for i in range(n):
    a, b = map(int, input().split())
    if (i+1)+ a > n:
        continue
    else:
        scehdule.append((a,b))
dp = [0 for i in range(n+1)]
for i in range(n):
    for j in range(i + scehdule[i][0], n+1):
        if dp[j] < dp[i] + scehdule[i][1]: 
            dp[j] = dp[i] + scehdule[i][1]
print(dp[-1])
#https://great-park.tistory.com/48