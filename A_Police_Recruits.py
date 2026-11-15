n = int(input())
arr = list(map(int, input().split()))

p_c = 0
c_c = 0

for i in arr:
    if i==-1:
        if p_c>0:
            p_c-=1
        else:
            c_c+=1
    else:
        p_c+=i
print(c_c)