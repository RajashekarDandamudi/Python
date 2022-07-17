from unittest.main import MAIN_EXAMPLES


a="bananna"
b="ball"

a="meals"
b="meal"

first_charecter=    a[:3]
second_charecter=   b[:2]

Res1=(first_charecter==second_charecter) and (first_charecter == second_charecter)
Res2=(first_charecter==second_charecter) or (first_charecter != second_charecter)
#Res=(first_charecter==second_charecter) not (first_charecter != second_charecter)
result=(Res1+Res2)

print(result)