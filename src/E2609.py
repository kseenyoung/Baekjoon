a, b = list(map(int, input().split()))
numa = []
numb = []

for i in range(1, min(a, b)+1):
    if a % i == 0:
        numa.append(i)
    if b % i == 0:
        numb.append(i)

numa.reverse()
numb.reverse()

for i in numa:
    for j in numb:
        if i == j:
            print(i)                        #최대공약수
            print(int(i*(a / i)*(b / i)))   #최소공배수 #(a*b)/i
            exit()