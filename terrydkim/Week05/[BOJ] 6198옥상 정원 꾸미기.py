import sys
input = sys.stdin.readline

N = int(input())
H = [int(input()) for i in range(N)]

stack = []
cnt = 0

for i in H:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    # 내가 관찰 당하는 옥상 수
    cnt += len(stack)-1
print(cnt)

# 시간떄문에 안되는줄 알면서 그냥 해보기
# lst = [0] * (N-1)
# for i in range(N-1):
#     for j in range(i+1,N):
#         if H[i] < H[j]:
#             lst[i] = j-i-1
#             break
#         if j == N-1:
#             lst[i] = j-i
# print(sum(lst))
