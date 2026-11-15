t = int(input())

for _ in range(t):
    n = int(input())

    if n > 45:
        print(-1)
        continue

    ans = []

    for digit in range(9, 0, -1):
        if n >= digit:
            ans.append(str(digit))
            n -= digit

    print("".join(ans[::-1]))