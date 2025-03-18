queue = []
# stack = []

num = int(input())
cmd = []
for i in range(num):
    cmd.append(input())
# print(cmd)

for i in cmd:
    if i[0] == '+':
        val = i[len(i)-1]
        queue.append(val)
        # print('+' + val + ':', queue)
    elif i[0] == '-':
        if len(queue) == 0:
            print('None')
        else:
            queue.pop(0)
            # print('-' + queue.pop(0) + ':', queue)

# for i in cmd:
#     if i[0] == '+':
#         val = i[len(i)-1]
#         stack.append(val)
#         print('+' + val + ':', stack)
#     elif i[0] == '-':
#         if len(stack) == 0:
#             print('None')
#         else:
#             print('-' + stack.pop() + ':', stack)

print(queue)
# print(stack)