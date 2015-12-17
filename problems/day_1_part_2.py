from data.day_1 import parens

floor = 0
for position, paren in enumerate(parens):
    if paren == "(":
        floor += 1
    elif paren == ")":
        floor -= 1
    if floor < 0:
        break
# the first character of a multiline string is \n
print(position)
