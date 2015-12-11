from data.day_1 import parens

position = 0
floor = 0
for paren in parens:
    if paren == "(":
        floor += 1
        position += 1
    elif paren == ")":
        floor -= 1
        position += 1
    if floor < 0:
        print(position)
        break
