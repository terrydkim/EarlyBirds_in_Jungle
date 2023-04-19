import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst = deque(lst)
    idx = list(range(N))
    idx = deque(idx)
    count = 0
    while lst:
        cnt = 0
        x = lst.popleft()
        y = idx.popleft()
        for i in range(len(lst)):
            if x < lst[i] :
                lst.append(x)
                idx.append(y)
                cnt += 1
                break

        if cnt == 0 :
            count += 1
            if y == M:
                print(count)

# enumerate 사용
'''import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    lst = enumerate(lst)
    lst = deque(lst)

    count = 0
    while lst:
        cnt = 0
        y, x = lst.popleft()

        for i in range(len(lst)):
            if x < lst[i][1] :
                lst.append((y,x))
                cnt += 1
                break

        if cnt == 0 :
            count += 1
            if y == M:
                print(count)

'''
