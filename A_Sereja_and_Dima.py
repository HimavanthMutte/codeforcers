n = int(input())

arr = list(map(int, input().split()))

i , j = 0, n - 1 

turn = 0 

score_0 , score_1 = 0 , 0

while i <= j:
    if arr[i] > arr[j]:
        if turn==0:
            score_0 += arr[i]
        else:
            score_1 += arr[i]
        i+=1 
    else:
        if turn==0:
            score_0 += arr[j]
        else:
            score_1 += arr[j]
        j-=1
    turn = 1 - turn
print(score_0, score_1)