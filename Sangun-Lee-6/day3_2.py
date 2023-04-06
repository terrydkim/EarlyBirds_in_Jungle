import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    stack.append(int(input()))


cnt = 0
for i in range(len(stack)):
    
    for j in range(i+1, len(stack)):
        if stack[i] <= stack[j]:
            break
        elif stack[i] > stack[j]:
            cnt += 1

print(cnt)