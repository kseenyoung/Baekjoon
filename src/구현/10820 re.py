import sys

input = sys.stdin.readline

for line in sys.stdin:
    try:
        alist = [0] * 4
        line = line.strip('\n')
        for i in line:
            if i.islower():
                alist[0] += 1
            elif i.isupper():
                alist[1] += 1
            elif i.isdigit():
                alist[2] += 1
            elif i.isspace():
                alist[3] += 1
        print(alist[0], alist[1], alist[2], alist[3])
    except EOFError:
        break

