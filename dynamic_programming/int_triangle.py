# boj_1932

import sys
n = int(input())

dp = []

for i in range(n):
    numbers = list(map(int,input().split(" ")))
    dp.append(numbers)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j]+=dp[i-1][j]
        elif j==i:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j]+=max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[n-1]))