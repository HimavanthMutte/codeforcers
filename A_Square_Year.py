def bs_sqrt(n):
    low, high = 0, n

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1

    return -1

tot = int(input())

for _ in range(tot):
    num = input()
    num.strip()
    n = int(num)

    res = bs_sqrt(n)

    if res != -1:
        print(res , 0)
    else:
        print(-1)