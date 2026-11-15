tot = int(input())

for _ in range(tot):
    n = int(input())
    arr = list(map(int, input().split()))

    print(len(set(arr)))