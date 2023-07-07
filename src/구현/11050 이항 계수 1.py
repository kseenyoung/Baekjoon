N, K = map(int, input().split())
dp = [0]*11

def factorial(n):
    if n == 1 or n == 0:
        return 1
    if dp[n] == 0:
        dp[n] = n * factorial(n-1)
    return dp[n]

division = (factorial(N-K)*factorial(K))
if division != 0:
    print(factorial(N)//division)
else:
    print(0)