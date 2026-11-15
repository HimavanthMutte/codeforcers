n = int(input())

cnt = 0

for i in range(n):
    sym = input()
    if sym == "++X" or sym == "X++":
        cnt += 1
    else:
        cnt -= 1
print(cnt)