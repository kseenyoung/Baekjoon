n = int(input())

# goldbach = [False, False] + [True]*10000000
# for i in range(2, 5001):
#     for j in range(i+i, 10000001, i):
#         goldbach[j] = False

# print(goldbach)
if n != 1:
    a = 2
    while True:
        if n % a == 0:
            print(a)
            n //= a
            if n == 1:
                break
        else:
            a += 1

