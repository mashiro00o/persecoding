x = int(input())
y = int(input())

if x > y:
    larger_num = x
    smaller_num = y
else:
    larger_num = y
    smaller_num = x

difference = larger_num - smaller_num
print(difference)
