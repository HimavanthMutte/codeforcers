a = input()
b = input()

n = len(a)


for i in range(n):
    if a[i] != b[i]:
        x , y = a[i], b[i]
        if (x.lower() < y.lower()):
            print(-1)
            break
        else:
            print(1)
            break

        