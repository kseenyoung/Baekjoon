N = int(input())
dp = [0]*1001

# SK == 0, CY == 1
dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, N+1):
    dp[i] = 1 if dp[i-1] == 0 else 0

print('SK' if dp[N] == 0 else 'CY')임