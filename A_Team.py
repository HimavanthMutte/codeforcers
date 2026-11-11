n = int(input())

cnt = 0 

for i in range(n):
    arr = list(map(int, input().split()))
    if arr.count(1) >= 2:
        cnt += 1
print(cnt)