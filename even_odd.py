from math import remainder


a=int(input())

Remainder = a % 2

is_even = Remainder == 0

if Remainder != 0:
    print("even")
else:
    print("odd")