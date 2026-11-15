string = input()

arr = list(map(int, string.split("+")))

arr.sort()

print("+".join(map(str, arr)))