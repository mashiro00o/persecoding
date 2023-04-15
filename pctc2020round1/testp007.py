house1 = int(input())
house2 = int(input())
house3 = int(input())

if house1 <= 100 and house1 >= 51: # check for side 1
    if house1 % 2 == 0:
        side1 = "east"
    else:
        side1 = "west"
else:
    if house1 % 2 == 0:
        side1 = "north"
    else:
        side1 = "south"

if house2 <= 100 and house2 >= 51: # check for side 2
    if house2 % 2 == 0:
        side2 = "east"
    else:
        side2 = "west"
else:
    if house2 % 2 == 0:
        side2 = "north"
    else:
        side2 = "south"

if house3 <= 100 and house3 >= 51: # check for side 3
    if house3 % 2 == 0:
        side3 = "east"
    else:
        side3 = "west"
else:
    if house3 % 2 == 0:
        side3 = "north"
    else:
      side3 = "south"


print(side1)
print(side2)
print(side3)
