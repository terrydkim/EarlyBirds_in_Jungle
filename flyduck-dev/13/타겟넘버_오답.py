import sys
sys.setrecursionlimit(10**6)
def solution(numbers, target):
    global sum,answer
    sum = 0
    answer = 0
    def dfs(num, idx):
        print(num)
        global sum,answer
        sum = sum + num
        if idx == len(numbers)-1 and sum == target:
            answer = answer +1
            return
        if idx == len(numbers)-1:
            return
        for k in range(idx+1, len(numbers)):
            dfs(numbers[k], k)
            dfs(-numbers[k], k)
        
    sum = 0
    dfs(-numbers[0],0)
    sum = 0
    dfs(+numbers[0],0)
    return answer