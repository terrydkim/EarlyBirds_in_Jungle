import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
buildings = deque([int(input()) for _ in range(n)])

stack = []
tot = 0

for building in buildings:
    while stack and building <= stack[-1]:
        stack.pop()
    # stack에 들어가는거 - 높이가 낮은거, 아무것도 없을 때
    stack.append(building)

    tot += len(stack)



