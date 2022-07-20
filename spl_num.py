a = input()

x = (int(a[0])+int(a[1])) == 7
y = (int(a[0])== 7) or (int(a[1])== 7) 
z = (int(a) % 7) == 0

if (x or y )or z:
    print("Special Number")
else:
    print("Normal Number")