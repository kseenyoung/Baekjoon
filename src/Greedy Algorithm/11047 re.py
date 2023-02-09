import sys

input = sys.stdin.readline

N, money = map(int, input().split())
coins = []
result = 0
for _ in range(N):
    coins.append(int(input()))

for r in reversed(coins):
    if money == 0:
        break
    result += money//r
    money %= r

print(result)