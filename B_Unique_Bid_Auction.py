tot = int(input())

for _ in range(tot):
    n = int(input())
    arr = list(map(int, input().split()))
    m = {}
    for i in arr:
        m[i] = m.get(i, 0) + 1
    mini = float('inf')
    for k, v in m.items():
        if v == 1:
            mini = min(mini, k)
    if mini == float('inf'):
        print(-1)
    else:
        print(arr.index(mini) + 1)
    