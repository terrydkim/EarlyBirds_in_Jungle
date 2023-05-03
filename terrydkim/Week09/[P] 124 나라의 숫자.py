from collections import deque
def solution(n):
    answer = deque()
    while n:
        a = n % 3
        if a == 0:
            n -= 1
            answer.appendleft('4')
        else:
            answer.appendleft(str(a))
        n //= 3
    return ''.join(answer)