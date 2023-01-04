N, M = list(map(int, input().split()))
alist = list(map(int, input().split()))
maxN = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = alist[i] + alist[j] + alist[k]
            if M >= temp > maxN:
                maxN = temp

print(maxN)