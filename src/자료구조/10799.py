alist = input()

stack = []
temp = False  # True (, False )
result = 0

for a in alist:
    if a == "(":
        stack.append(a)
        temp = True
    elif a == ')':
        if temp:
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
        temp = False


print(result)