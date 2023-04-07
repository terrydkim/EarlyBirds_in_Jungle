import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    heapq.heappush(cards, a+b)

print(sum(cards))