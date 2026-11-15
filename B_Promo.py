
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

for _ in range(m):
    x, y = map(int, input().split())

    print(prefix[n - y] - prefix[n - x])
