tot = int(input())

for _ in range(tot):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    for i, x in enumerate(arr):
        if freq[x] == 1:
            print(i + 1)
            break