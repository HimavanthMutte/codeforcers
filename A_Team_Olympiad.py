n = int(input())
arr = list(map(int, input().split()))

coding = []
maths = []
pe = []

for i, skill in enumerate(arr, start=1):
    if skill == 1:
        coding.append(i)
    elif skill == 2:
        maths.append(i)
    else:
        pe.append(i)

k = min(len(coding), len(maths), len(pe))

print(k)

for i in range(k):
    print(coding[i], maths[i], pe[i])