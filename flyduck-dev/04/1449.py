import sys
input = sys.stdin.readline
N, L = map(int,input().split())
pos = [int(j)for j in input().split()] 
pos.sort()
end = pos[0] + L - 1
count = 1
for i in range(1, N):
    if end < pos[i]:
        count += 1
        end = pos[i] + L - 1

print(count)