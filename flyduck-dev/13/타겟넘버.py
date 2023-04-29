import sys
sys.setrecursionlimit(10**6)
def solution(numbers, target):
    global answer
    answer = 0
    def dfs(total, idx,length):
        global answer
        if idx == length and total == target:
            answer = answer +1
            return
        if idx == length:
            return
        dfs(total + numbers[idx+1], idx+1,length)
        dfs(total - numbers[idx+1], idx+1,length)
        
    dfs(-numbers[0],0,len(numbers)-1)
    dfs(+numbers[0],0,len(numbers)-1)
    return answer