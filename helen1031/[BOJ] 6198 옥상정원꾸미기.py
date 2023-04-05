import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
buildings = deque([int(input()) for _ in range(n)])

stack = []
tot = 0

for building in buildings:
    while stack and stack[-1] <= building:
        stack.pop()
    stack.append(building)

    tot += len(stack) - 1
    
print(tot)
