import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ylist = []
xlist = []
for _ in range(m):
    y, x = map(int, input().split())
    ylist.append(y)
    xlist.append(x)

yy, xx = round(sum(ylist) / m), round(sum(xlist) / m)

dist = 0
for i in range(m):
    dist += abs(ylist[i] - yy)
    dist += abs(xlist[i] - xx)

print(dist)