import sys
input = sys.stdin.readline
N, L = map(int,input().split()) # 가게 이름 후보의 수 N, 가게 이름의 길이 L (1 <= N, L <= 20)
names =[] 
for i in range(N):
    a = input().strip()
    names.append(a)

answer = None
for i in range(L):
    for j in range(ord('A'), ord('Z') + 1):
        target = names[0][:i] + chr(j) + names[0][i+1:]
        isOK = True
        for name in names:
            cnt = 0
            for k in range(L):
                if target[k] != name[k]:
                    cnt += 1
                    if cnt > 1:
                        isOK = False
                        break
            if not isOK:
                break
        if isOK:
            answer = target
            break
    if answer is not None:
        break

if answer is not None:
    print(answer)
else:
    print("CALL FRIEND")

