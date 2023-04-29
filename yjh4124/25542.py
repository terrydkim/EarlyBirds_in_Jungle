import sys

sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')


n,l_name=map(int,input().split())

data=[[data for data in input()] for _ in range(n)]

# for i in data:
#     print(i)

idx=0

check=[0 for _ in range(l_name)]

result=[0 for _ in range(l_name)]

if n==1:
    for elem in data[0]:
        print(elem,end='')

elif n>=2:
    while (sum(check)!=l_name) and idx<=n-2:
        name=data[idx]
        next_name=data[idx+1] 
        cnt=sum(check)
        for j in range(l_name):
            if check[j]==0:
                if name[j]==next_name[j]:
                    cnt+=1
                    check[j]=1
                    result[j]=name[j]
        idx=idx+1

    if sum(check)!=l_name: print('CALL FRIEND')
    elif sum(check)==l_name:
        for data in data:
            cnt=0
            for i in range(l_name):
                if data[i]==result[i]:
                    cnt+=1
            if cnt<=l_name-2: 
                print('CALL FRIEND')
                break
        else:
            for elem in result:
                print(elem,end='')
        

