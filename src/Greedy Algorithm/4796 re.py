import sys

input = sys.stdin.readline
i = 1

while True:
    days = list(map(int, input().split()))
    if days == [0, 0, 0]:
        break

    d, m = divmod(days[2], days[1])
    result = d*days[0] + min(m, days[0])
    print("Case %d: %d" % (i, result))
    i += 1
