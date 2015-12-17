from data.day_2 import boxes

boxes = [box for box in boxes if box != '']
dimensions = [box.split('x') for box in boxes]
faces = [
    (int(box[0]) * int(box[1]),
     int(box[1]) * int(box[2]),
     int(box[2]) * int(box[0]))
    for box in dimensions]
square_feet = [
    2*sum(box) + min(box)
    for box in faces]
print(sum(square_feet))
