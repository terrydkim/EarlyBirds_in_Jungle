import sys
input = sys.stdin.readline
H,W = map(int,input().split())
blocks = [int(i) for i in input().split()]

stack = []
answer = 0
max_height = 0
for i in range(W):
    cnt = 0
    while stack and stack[-1] < blocks[i]: 
        if blocks[i] > max_height:
            answer += max_height - stack.pop()
        else: 
            answer += blocks[i]-stack.pop()
            cnt += 1
    if cnt:
        for j in range(cnt):
            stack.append(blocks[i])

    max_height = max(max_height, blocks[i])
    stack.append(blocks[i])
print(answer)