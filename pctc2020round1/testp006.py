car_type = input()

if car_type != "electric":
    engine_size = float(input())

if car_type == "electric":
    tax_due = 0
elif car_type == "hybrid":
    if engine_size < 1.8:
        tax_due = 120
    else:
        tax_due = 140
elif car_type == "petrol":
    if engine_size < 1.8:
        tax_due = 150
    else:
        tax_due = 170
elif car_type == "diesel":
    if engine_size < 1.8:
        tax_due = 180
    else:
        tax_due = 200

print("${:.0f}".format(tax_due))
