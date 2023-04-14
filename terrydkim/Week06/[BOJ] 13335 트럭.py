import sys
from collections import deque
input = sys.stdin.readline

#트럭 수, 다리길이, 최대 하중
n,w,L = map(int,input().split())

truck = list(map(int,input().split()))
q = deque(truck)

result = 0
while q:
    cnt = 0
    a = q.popleft()
    cnt += a
    xcnt = 1
    while q:
        x = q.popleft()
        cnt += x
        if cnt > L:
            q.appendleft(x)
            cnt -= x
            break
        xcnt += 1
    if q:     
        result += w + xcnt -1 
    else :
        result += w + xcnt
# 다음 트럭에 나가면서 동시에 들어오는 코드 구현해야함
print(result)