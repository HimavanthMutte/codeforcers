n , k = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0

k = arr[k-1]

for i in arr:
    if i>=k and i!=0:
        cnt += 1
print(cnt)