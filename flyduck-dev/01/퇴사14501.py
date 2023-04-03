# 반례 케이스를 잡지 못했습니다!😂

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
for i in range(len(scehdule)):
    end_day = i + scehdule[i][0]
    dp[end_day] = max(dp[end_day], dp[i] + scehdule[i][1])
print(max(dp))
