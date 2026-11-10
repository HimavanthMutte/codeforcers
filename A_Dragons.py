s,n = map(int,input().split())

arr = []

for _ in range(n):
    x , y = map(int,input().split())
    arr.append((x,y))

arr.sort()

for i in range(n):
    if (s <= arr[i][0]):
        print("NO")
        exit()
    else:
        s += arr[i][1]
print("YES")