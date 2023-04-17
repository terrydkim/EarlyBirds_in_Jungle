import sys
input = sys.stdin.readline

from collections import Counter

r, c, k = map(int, input().split())
r, c = r-1, c-1

a = [list(map(int, input().split())) for _ in range(3)]

time = 0

while True:
    if a[r][c] == k:
        break

    if time == 2:
        break

    if len(a) >= len(a[0]):
        maxc = 0
        for i, ya in enumerate(a):
            counter = Counter(ya)

            tmp = []
            for cntr in counter.items():
                tmp.append((cntr[0], cntr[1]))
            tmp.sort(key = lambda x: (x[1], x[0]))

            nya = []
            for t in tmp:
                nya.append(t[0])
                nya.append(t[1])
            a[i] = nya
            maxc = max(maxc, len(a[i]))

        for i, ya in enumerate(a):
            while len(ya) < maxc:
                ya.append(0)

    else:
        print(a)
        maxr = 3
        for x in range(len(a[0])):
            ylist = []
            for y in range(len(a)):
                ylist.append(a[y][x])

            counter = Counter(ylist)
            tmp = []
            for cntr in counter.items():
                tmp.append((cntr[0], cntr[1]))
            tmp.sort(key=lambda x: (x[1], x[0]))

            nxa = []
            for t in tmp:
                nxa.append(t[0])
                nxa.append(t[1])

            print(nxa)
            for i in range(len(nxa)):
                if i < len(a):
                    a[i][x] = nxa[i]
                else:
                    a.append([nxa[i]])
            maxr = max(maxr, len(a))
            print(a)

    time += 1
print(time)