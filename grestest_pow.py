#a = int(input())
#b = int(input())

a=2
b=3

is_greatest = (a ** b)
is_lowest = (b ** a)

Greatest = (is_greatest > is_lowest)

if Greatest:
    print(is_greatest)
else:
    print(is_lowest)