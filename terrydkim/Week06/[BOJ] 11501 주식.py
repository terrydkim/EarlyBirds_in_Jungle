import sys
input = sys.stdin.readline

T = int(input())
for k in range(T):
    n = int(input())
    cost = list(map(int,input().split()))
    big = cost[-1]
    cnt = 0
    for i in range(n-1,-1,-1):
        if big == cost[i] :
            continue
        elif big < cost[i] :
            big = cost[i]
        else :
            cnt += big - cost[i]
    print(cnt)