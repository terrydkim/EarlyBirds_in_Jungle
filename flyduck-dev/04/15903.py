import sys
input = sys.stdin.readline
n, m = map(int,input().split())
cards = [int(i) for i in input().split()]
cards.sort()
cnt = 0
bin_arr = []
for i in range(n):
    while len(bin_arr) <= 2 and cnt <= m:
            cnt += 1
            k = sum(cards)
            cards.pop()
            cards.pop()
            cards.append(k)
            cards.append(k)

    bin_arr.append(cards[i])
print(sum(cards))