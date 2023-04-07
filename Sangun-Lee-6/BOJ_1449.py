import sys
input = sys.stdin.readline

N, L = map(int, input().split())
position_lst = list(map(int, input().split()))
position_lst.sort()

cnt = 0
end = 0

for p in position_lst:
    if end <= p-0.5:
        cnt += 1
        end = p -0.5 + L
print(cnt)