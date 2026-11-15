n, time = map(int, input().split())

time_in_minutes = 240 - time

i = 1
cnt = 0

while i * 5 <= time_in_minutes and cnt < n:
    cnt += 1
    time_in_minutes -= i * 5
    i += 1

print(cnt)