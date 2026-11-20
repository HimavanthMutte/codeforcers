
def solve():
    s = input().strip()

    if '0' not in s:
        print(0)
    elif '1' not in s:
        print(1)
    else:
        first = s.find('0')
        last = s.rfind('0')

        if '1' not in s[first:last + 1]:
            print(1)
        else:
            print(2)


t = int(input())

for _ in range(t):
    solve()
