from collections import deque

def solution(queue1, queue2):
    answer = -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    length = len(queue1)
    x = sum(queue1)
    y = sum(queue2)
    while (x != y):
        if cnt > length*4:
            return answer
        if x > y:
            a = queue1.popleft()
            queue2.append(a)
            x -= a
            y += a
            cnt += 1
        elif y > x :
            b = queue2.popleft()
            queue1.append(b)
            x += b
            y -= b
            cnt += 1
    answer = cnt
        
    return answer


