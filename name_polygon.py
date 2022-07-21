first_lline = int(input())

if first_lline < 3:
    print("Not Polygon")
elif first_lline == 3:
        print("Triangle")
elif first_lline == 4:
    print("Quadrilateral")
elif first_lline == 5:
    print("Pentagon")
else:
    print("Big Polygon")