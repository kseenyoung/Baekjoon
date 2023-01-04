N = int(input())
codeS = list(input())
result = 0

for i in range(N):
    result += (ord(codeS[i]) - 96)*(31**i)

print(result % 1234567891)