import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


raw = input().split()

data = sorted(raw, key=len)

print(data)

len_ = len(data)

answer=True

for idx in range(len_):
    for jdx in range(idx+1, len_):

        left_pi = 0
        left_pj = 0
        size_idata = len(data[idx])
        size_jdata = len(data[jdx])

        print(data[idx], data[jdx])
        print("------")

        while (left_pj+size_idata <= size_jdata-1):

            if (data[idx][left_pi] == data[jdx][left_pj]):
                cnt = 0

                for alpha in range(size_idata):
                    if (data[idx][left_pi+alpha] == data[jdx][left_pj+alpha]):
                        cnt += 1
                    elif (data[idx][left_pi+alpha] != data[jdx][left_pj+alpha]):
                        break

                if (cnt == size_idata):
                    answer = False
                    break
                else:
                    left_pj += 1

            elif (data[idx][left_pi] != data[jdx][left_pj]):
                left_pj+=1


print(answer)
