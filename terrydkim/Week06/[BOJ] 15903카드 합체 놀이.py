import sys, heapq
input = sys.stdin.readline


n,m = map(int,input().split())
lst = list(map(int,input().split()))
heapq.heapify(lst)

for i in range(m):
    x = heapq.heappop(lst)
    y = heapq.heappop(lst)
    heapq.heappush(lst, x+y)
    heapq.heappush(lst, y+x)

print(sum(lst))