n = int(input())
result = []
if n == 0:  # 입력 값이 0일 때
    print(0)
else:
    while n != 0:
        mod = n % -2
        result.append(-mod)
        n //= -2
        if mod:  # 나머지가 0이 아니라면
            n += 1
        print("n : %d, mod : %d" % (n, mod))

    for r in reversed(result):
        print(r, end="")
