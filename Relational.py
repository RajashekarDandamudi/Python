a=str()
b=str()

a="raja"
b="rani"

c= a[:0] == b[:0]#Double equal
C= a[:3] != b[:3]#Not equal
d= a[:2] >= b[:2]#greaterthan or equal
D= a[:2] <= b[:2]#lessthan or equal

print(c,C,d,D)