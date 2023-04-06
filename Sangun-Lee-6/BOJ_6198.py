n = int(input())
 
arr = [int(input()) for i in range(n)]
stk = []
ans = 0
 
for i in range(n):
    while stk and stk[-1] <= arr[i]:
        stk.pop()
 
    stk.append(arr[i])
    ans += len(stk) -1 
    # 자기 자신은 뺴주기
 
print(ans)