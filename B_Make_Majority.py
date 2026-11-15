
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    arr = []

    for ch in s:
        if ch == '0' and arr and arr[-1] == '0':
            continue
        arr.append(ch)

    ones = arr.count('1')
    zeros = arr.count('0')

    print("Yes" if ones > zeros else "No")
