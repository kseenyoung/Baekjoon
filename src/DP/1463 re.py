n = int(input())

if n == 1:
    print(0)
else:
    alist = [0] * (n + 1)
    alist[1] = 0

    for i in range(2, n+1):

        answer = alist[i-1] + 1
        if i % 3 == 0:
            answer = min(answer, alist[i//3] + 1)
        if i % 2 == 0:
            answer = min(answer, alist[i//2] + 1)
        alist[i] = answer

    print(alist[n])