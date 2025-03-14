num = int(input())
stack = []
min_stk = []

for _ in range(num):
    ipt = list(input().split( ))
    if ipt[0] == 'PUSH':
        stack.append(int(ipt[1]))
        if min_stk == [] or stack[-1] < min_stk[-1]:
            min_stk.append(int(ipt[1]))
    elif ipt[0] == 'POP':
        if not stack or not min_stk:
            print('EMPTY')
        else:
            if stack[-1] == min_stk[-1]:
                min_stk.pop()
            stack.pop()
    else:
        if not min_stk:
            print('EMPTY')
        else:
            print(min_stk[-1])