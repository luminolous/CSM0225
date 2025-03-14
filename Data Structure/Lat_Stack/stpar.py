def can_reorder_trucks(n, trucks):
    stack = []
    expected = 1
    for truck in trucks:
        while stack and stack[-1] == expected:
            expected += 1
            stack.pop()
        if truck == expected:
            expected += 1
        else:
            stack.append(truck)
    while stack and stack[-1] == expected:
        expected += 1
        stack.pop()
    return expected == n + 1

res = []
while True:
    n = int(input())
    if n == 0:
        break
    trucks = list(map(int, input().split()))
    if can_reorder_trucks(n, trucks):
        res.append("yes")
    else:
        res.append("no")

for i in res:
    print(i)