s = input() 
count_l , count_u = 0, 0 
for i in s:
    num = ord(i)
    if num>=97 and num<=123:
        count_l+=1
    else:
        count_u+=1
if count_l >= count_u:
    print(s.lower())
else:
    print(s.upper())