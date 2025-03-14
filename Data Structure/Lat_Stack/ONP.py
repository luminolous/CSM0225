def ting(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def rpn(exp):
    stack = []
    res = []
    for char in exp:
        if char.isalpha():
            res.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()
        else:
            while stack and ting(stack[-1]) >= ting(char):
                res.append(stack.pop())
            stack.append(char)
    while stack:
        res.append(stack.pop())
    return ''.join(res)

t = int(input())
output = []
for _ in range(t):
    exp = input().strip()
    output.append(rpn(exp))

for i in output:
    print(i)