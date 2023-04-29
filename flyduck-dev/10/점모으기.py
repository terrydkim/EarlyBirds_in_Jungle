import sys
input = sys.stdin.readline

N, M = map(int,input().split())
x_li = []
y_li = []
for i in range(M):
    x, y = map(int,input().split())
    x_li.append(x)
    y_li.append(y)

x_li.sort()
y_li.sort()

mid_idx = M //2
mid_x = x_li[mid_idx]
mid_y = y_li[mid_idx]

dis = 0
for i in range(M):
    dis += abs(mid_x - x_li[i])
    dis += abs(mid_y - y_li[i])
print(dis)