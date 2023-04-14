## 틀린 문제

def check(arr1, arr2):
    
    cnt = 0
    for i in range(len(arr1)):
        
        if arr1[i] != arr2[i]:
            cnt += 1
    return cnt

import sys
input = sys.stdin.readline

N, L = map(int, input().split())

name = [[] for _ in range(N)]
for i in range(N):
    name[i] = list(map(str, input().rstrip()))



for j in range(N):
    flag = False    
    for k in range(N):
        
        cnt = check(name[j], name[k])

        if cnt >= 2:
            flag = True
            break
    
    if flag:
        continue
    else :
        print(*name[j], sep='')
        exit(0)

print('CALL FRIEND')
    


