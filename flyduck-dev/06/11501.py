import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    s = int(input())
    arr = list(map(int, input().split()))
    wallet = 0
    max_val = arr[-1]
    for k in range(len(arr)-2, -1, -1):
        if max_val > arr[k]:
            wallet += max_val-arr[k]
        else:
            max_val = arr[k]
    print(wallet)