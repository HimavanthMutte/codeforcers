n , m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

mini = float('inf')

profit = 0

for i in range(m):
    profit += arr[i]
    mini = min(mini,profit)

print(abs(mini))