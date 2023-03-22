S = int(input())

if S==1 or S==2:  # attention
    print(1)
else:
    sum = 0

    for i in range(1, S):
        sum += i
        if sum > S:
            print(i-1)
            break
        if sum == S:
            print(i)
            break
