import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())

for _ in range(t):

    n = int(input())

    data = [[int(data) for data in sys.stdin.readline().split()]
            for _ in range(2)]

    # for i in data:
    #     print (i)

    res = 0
    res2 = 0

    xp = 0
    yp = -1

    if n == 1:
        if data[0][0] >= data[1][0]:
            res += data[0][0]
        else:
            res += data[1][0]

    elif n == 2:
        if data[0][0]+data[1][1] >= data[1][0]+data[0][1]:
            res += data[0][0]+data[1][1]
        else:
            res += data[1][0]+data[0][1]

    else:
        while yp <= n-3:
            if yp == -1:
                if xp == 0:
                    res += data[xp][yp+1]
                    yp += 1

            elif yp >= 0:
                if xp == 0:
                    if data[xp+1][yp+1]+data[xp][yp+2] >= data[xp+1][yp+2]:
                        res += data[xp+1][yp+1]
                        xp += 1
                        yp += 1
                    else:
                        res += data[xp+1][yp+2]
                        xp += 1
                        yp += 2

                elif xp == 1:
                    if data[xp-1][yp+1]+data[xp][yp+2] >= data[xp-1][yp+2]:
                        res += data[xp-1][yp+1]
                        xp -= 1
                        yp += 1
                    else:
                        res += data[xp-1][yp+2]
                        xp -= 1
                        yp += 2

        if yp == n-2:
            if xp == 0:
                res += data[xp+1][yp+1]
                yp += 1
            elif xp == 1:
                res += data[xp-1][yp+1]
                yp += 1

        xp = 0
        yp = -1
        while yp <= n-3:
            if yp == -1:
                if xp == 0:
                    res2 += data[xp+1][yp+1]
                    xp += 1
                    yp += 1

            elif yp >= 0:
                if xp == 0:
                    if data[xp+1][yp+1]+data[xp][yp+2] >= data[xp+1][yp+2]:
                        res2 += data[xp+1][yp+1]
                        xp += 1
                        yp += 1
                    else:
                        res2 += data[xp+1][yp+2]
                        xp += 1
                        yp += 2

                elif xp == 1:
                    if data[xp-1][yp+1]+data[xp][yp+2] >= data[xp-1][yp+2]:
                        res2 += data[xp-1][yp+1]
                        xp -= 1
                        yp += 1
                    else:
                        res2 += data[xp-1][yp+2]
                        xp -= 1
                        yp += 2

        if yp == n-2:
            if xp == 0:
                res2 += data[xp+1][yp+1]
                yp += 1
            elif xp == 1:
                res2 += data[xp-1][yp+1]
                yp += 1

    print(max(res, res2))
    # print(res, res2)
