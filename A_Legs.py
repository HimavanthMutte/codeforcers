tot = int(input())

for _ in range(tot):
    n = int(input())
    cows = n//4
    n = n%4
    hens = n//2
    print(cows+hens) 