tot = int(input())

for _ in range(tot):
    n = int(input())
    arr = input()
    dot_count = 0 
    flag = False
    consecutive_dot_count = 0
    for i in arr:
        if i==".":
            consecutive_dot_count+=1
            if consecutive_dot_count==3:
                flag = True 
            dot_count+=1
        else:
            consecutive_dot_count = 0   
    if flag:
        print(2)
    else:
        print(dot_count)