n, k = map(int, input().split())
l = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n + 1)]
dp[1] = 1
for i in range(1, n + 1):
    if i in a:
        dp[i] = 0
    else:
        for j in range(1, min(i, k + 1)):
            dp[i] += dp[i - j]
# print(dp, a)
print(dp[n])