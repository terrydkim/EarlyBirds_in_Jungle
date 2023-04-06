import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

see_li = []
stack = []
for i in range(0, n-1):
    stack.append(arr[i])
    see = 0
    for j in range(i+1, n):
        if stack[-1] > arr[j]:
            see+=1
        else:
            break
    see_li.append(see)

print(sum(see_li))
    

