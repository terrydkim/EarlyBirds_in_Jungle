import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card_lst = list(map(int, input().split()))

while (M>0):
    
    card_lst.sort()
    add_val = card_lst[0] + card_lst[1]
    card_lst[0] = card_lst[1] = add_val
    M -= 1

print(sum(card_lst))



