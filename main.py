stat = '12 2 3 4 * 10 5 / + * +'
stack = []
li = list(stat.split(' '))
ops = {'+': (lambda a, b: a + b),
       '-': (lambda a, b: a - b),
       '*': (lambda a, b: a * b),
       '/': (lambda a, b: b / a)
}

print(li)

for i in range(len(li)):
    try:
        li[i] = int(li[i])
    except ValueError:
        pass
    if isinstance(li[i], int):
        stack.append(li[i])
    else:
        stack.append(ops[li[i]](stack.pop(), stack.pop()))
    print(stack)






