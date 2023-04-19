def solution(numbers, target):
    n = len(numbers)
    dp = [[0] * 2001 for _ in range(n)]  # dp[i][j]: i번째까지의 숫자로 j를 만드는 경우의 수
    
    dp[0][1000-numbers[0]] = 1  # 첫 번째 숫자를 빼는 경우
    dp[0][1000+numbers[0]] = 1  # 첫 번째 숫자를 더하는 경우
    
    for i in range(1, n):
        for j in range(2001):
            if dp[i-1][j] > 0:
                dp[i][j+numbers[i]] += dp[i-1][j]  # 다음 숫자를 더하는 경우
                dp[i][j-numbers[i]] += dp[i-1][j]  # 다음 숫자를 빼는 경우
    
    return dp[n-1][1000+target]  # 마지막 숫자까지 사용하여 target을 만드는 경우의 수

