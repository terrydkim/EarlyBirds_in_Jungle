import sys
from collections import deque
input = sys.stdin.readline
n, w, L = map(int, input().split())
truck_arr = list(map(int, input().split()))

# while 문을 계속 돌리면서 다리가 큐
# 다리 위에 있는 트럭의 무게를 체크하고,
# 다리에 다음 트럭을 올릴 수 있는지 체크하고, 가능하면 올리고 day를 더해준다

bridge_q = deque()
day = 0
idx = 0
while idx!=len(truck_arr):
    if bridge_q and len(bridge_q) == w:
        bridge_q.popleft()
    if len(bridge_q) < w and L >= (sum(bridge_q) + truck_arr[idx]):# 위에 올라간 것들이랑 뒤에 오는 트럭 합산이 다리의 최대하중 보다 더 작다면
        bridge_q.append(truck_arr[idx])
        idx+=1
    else:
        bridge_q.append(0)
    day += 1
    if idx == n:
        break
print(day+ w)