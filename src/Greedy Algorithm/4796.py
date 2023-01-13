i = 1
while True:
    L, P, V = list(map(int, input().split()))
    if L == 0:
        break
    result = (V//P)*L
    result += min((V % P), L)
    print("Case %d:" % i, result)
    i += 1
