import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
for i in range(n):
    N, M = map(int, input().split()) 
    arr = list(map(int, input().split()))
    max_li = arr.copy()
    max_li.sort()
    q = deque()
    for i, num in enumerate(arr):
        q.append((i, num)) #deque([(0, 1), (1, 2), (2, 3), (3, 4)])
    cnt = 0
    while q:
        idx,num = q.popleft()
        if num == max_li[-1]:
            cnt += 1
            max_li.pop()
            if idx == M:
                print(cnt)
                break
        else:
            q.append((idx,num))