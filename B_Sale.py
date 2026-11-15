n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

profit = 0

for i in range(m):
    if arr[i] >= 0:
        break
    profit += arr[i]

print(abs(profit))