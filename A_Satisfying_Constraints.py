tot = int(input())
for _ in range(tot):
    n = int(input())
    
    type_3 = set() 
    mini = float('-inf')
    maxi = float('inf')  
    
    
    for i in range(n):
        t, num = map(int, input().split())
        if t == 1:
            mini = max(mini, num)
        elif t == 2:
            maxi = min(maxi, num)
        else:
            type_3.add(num)
            
    # 3. Handle case where bounds cross
    if mini > maxi:
        print(0)
    else:
        count = sum(1 for j in type_3 if mini <= j <= maxi)
        print(maxi - mini + 1 - count)
