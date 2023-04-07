import sys
input = sys.stdin.readline

N , L = map(int,input().split())

name = [input().strip() for i in range(N)]


result=[]

for i in range(N):
    for k in range(N):
        if i == k : 
            continue
        cnt = 0
        for j in range(L):
            if name[i][j] != name[k][j]:
                cnt += 1
            if cnt > 1 :
                break
        if cnt == 1:
            result.append(name[k])
            break
    if result:
        print(result[0])
        break
if not result:
    print('CALL FRIEND')
