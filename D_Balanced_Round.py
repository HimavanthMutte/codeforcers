tot = int(input())

for _ in range(tot):
    n , k = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()
    max_cnt = 1
    cnt = 1

    for i in range(n-1):
        if (abs(arr[i]-arr[i+1])<=k):
            cnt+=1
            max_cnt = max(max_cnt,cnt)
        else:
            cnt = 1

    print(n-max_cnt)