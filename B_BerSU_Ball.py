n = int(input())
boys = sorted(map(int, input().split()))

m = int(input())
girls = sorted(map(int, input().split()))

i = j = 0
pairs = 0

while i < n and j < m:

    diff = boys[i] - girls[j]

    if abs(diff) <= 1:
        pairs += 1
        i += 1
        j += 1

    elif diff < -1:
        i += 1

    else:
        j += 1

print(pairs)