tot = int(input())

for _ in range(tot):
    n = int(input())
    s = input()
    A_idx , B_idx = -1,-1
    for i in range(n):
        if s[i]=="A" and A_idx== -1:
            A_idx = i
        elif s[i]=="B":
            B_idx = i 
    if A_idx == -1 or B_idx == -1 or B_idx < A_idx:
        print(0)
    else:
        print(B_idx - A_idx)