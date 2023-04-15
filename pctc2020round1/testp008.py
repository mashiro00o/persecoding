days_until_fruit_day = int(input())
eat_by_days = []
while True:
    eat_by_day = int(input())
    if eat_by_day == -1:
        break
    eat_by_days.append(eat_by_day)

edible_fruits = sum(1 for eat_by_day in eat_by_days if eat_by_day >= days_until_fruit_day)
print(edible_fruits)
