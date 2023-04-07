import sys
input = sys.stdin.readline

N , L = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()


cnt =0
tape = 0
for i in lst:
    if i > cnt:
        cnt = i+L-1
        tape += 1

print(tape)