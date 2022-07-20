Word = input()

first_char = Word[0]

last_char = len(Word)-1

last_char = str(last_char)
 
no_of_stars = len(Word)-2

stars = "*" * no_of_stars

print(first_char + stars + last_char)