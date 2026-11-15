n = int(input())

m = {}
for _ in range(n):
    username = input()
    if username not in m:
        print("OK")
        m[username] = 1
    else:
        print(f"{username}{m[username]}")
        m[username] += 1