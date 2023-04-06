import sys
from collections import deque

sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

n=int(input())

data=[[data for data in input()] for _ in range(n)]

# for i in data:
#     print(i)

dx=(0, 1)
dy=(1,-1)


visit=[[0 for _ in range(n)] for _ in range(n)]


    
result=[]
res_max=0

for i in range(n):
    nowcandy=data[i][0]
    cnt=0
    for k in range(n):
        if (nowcandy==data[i][k]):
            nowcandy=data[i][k]
            cnt+=1

        elif (nowcandy!=data[i][k]):
            if (i+1<=n-1):
                if (data[i+1][k]==nowcandy):
                    nowcandy=data[i+1][k]
                    cnt+=1
                elif (data[i+1][k]!=nowcandy):
                    if (i-1>=0):
                        if (data[i-1][k]==nowcandy):
                            nowcandy=data[i-1][k]
                            cnt+=1
                        elif (data[i-1][k]!=nowcandy):
                            result.append((nowcandy,cnt))
                            res_max=max(res_max, cnt)
                            nowcandy=data[i][k]
                            cnt=1
                    elif (i-1<0):
                        result.append((nowcandy,cnt))
                        res_max=max(res_max, cnt)
                        nowcandy=data[i][k]
                        cnt=1

                    result.append((nowcandy,cnt))
                    res_max=max(res_max, cnt)
                    nowcandy=data[i][k]
                    cnt=1
            elif (i+1>n-1):
                if (i-1>=0):
                    if (data[i-1][k]==nowcandy):
                        nowcandy=data[i-1][k]
                        cnt+=1
                    elif (data[i-1][k]!=nowcandy):
                        result.append((nowcandy,cnt))
                        res_max=max(res_max, cnt)
                        nowcandy=data[i][k]
                        cnt=1
                elif (i-1<0):
                    result.append((nowcandy,cnt))
                    res_max=max(res_max, cnt)
                    nowcandy=data[i][k]
                    cnt=1

                result.append((nowcandy,cnt))
                res_max=max(res_max, cnt)
                nowcandy=data[i][k]
                cnt=1

    else: 
        result.append((nowcandy, cnt))            
        res_max=max(res_max, cnt)

for k in range(n):
    nowcandy=data[0][k]
    cnt=0
    for i in range(n):
        if (nowcandy==data[i][k]):
            nowcandy=data[i][k]
            cnt+=1
        elif (nowcandy!=data[i][k]):
            if (k+1<=n-1):
                if (data[i][k+1]==nowcandy):
                    nowcandy=data[i][k+1]
                    cnt+=1
                elif (data[i][k+1]!=nowcandy):
                    if (k-1>=0):
                        if (data[i][k-1]==nowcandy):
                            nowcandy=data[i][k-1]
                            cnt+=1
                        elif (data[i][k-1]!=nowcandy):
                            result.append((nowcandy,cnt))
                            res_max=max(res_max, cnt)
                            nowcandy=data[i][k]
                            cnt=1
                    elif (k-1<0):
                        result.append((nowcandy,cnt))
                        res_max=max(res_max, cnt)
                        nowcandy=data[i][k]
                        cnt=1

                    result.append((nowcandy,cnt))
                    res_max=max(res_max, cnt)
                    nowcandy=data[i][k]
                    cnt=1
            elif (k+1>n-1):
                if (k-1>=0):
                    if (data[i][k-1]==nowcandy):
                        nowcandy=data[i][k-1]
                        cnt+=1
                    elif (data[i][k-1]!=nowcandy):
                        result.append((nowcandy,cnt))
                        res_max=max(res_max, cnt)
                        nowcandy=data[i][k]
                        cnt=1
                elif (k-1<0):
                    result.append((nowcandy,cnt))
                    res_max=max(res_max, cnt)
                    nowcandy=data[i][k]
                    cnt=1

                result.append((nowcandy,cnt))
                res_max=max(res_max, cnt)
                nowcandy=data[i][k]
                cnt=1
    else: 
        result.append((nowcandy, cnt))
        res_max=max(res_max, cnt)

# print(result)

print(res_max)