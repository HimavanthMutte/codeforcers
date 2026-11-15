tot = int(input())

for _ in range(tot):
    word = input()
    length = len(word)
    if length <= 10:
        print(word)
    else:
        print(f"{word[0]}{length - 2}{word[-1]}")