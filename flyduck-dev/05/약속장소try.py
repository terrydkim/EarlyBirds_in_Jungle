import sys
input = sys.stdin.readline
N, L = map(int,input().split()) #가게 이름 후보의 수  N 가게 이름의 길이 L 1<=N, L<=20
isSTORE = False
answer = ""
names =[] 
for i in range(N):
    a = input().strip()
    names.append(a)

answer = []
for i in range(N): # 0 1 2 3 4
    isOK = True
    cnt = 0
    target = names[i]
    for j in range(0, N):
        if i==j:
            continue
        compare = names[j]
        cnt = 0
        for k in range(L):
            if target[k] != compare[k]:
                cnt +=1
            if cnt > 1:
                isOK = False
                break
        if isOK == False:
            break
        if cnt == 1:
            isOK = True
    if isOK == True:
        answer.append(target)
if answer:
    print(answer[0])
else:
    print("CALL FRIEND")