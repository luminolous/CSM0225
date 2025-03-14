num = int(input())
query = []

for i in range(num):
    ipt = list(map(int, input().split(' ')))
    if ipt[0] == 1:
        query.append(ipt[1])
    elif ipt[0] == 2:
        query.pop()
    elif ipt[0] == 3:
        if len(query) != 0:
            print(query[0])
        else:
            print('Empty!')
