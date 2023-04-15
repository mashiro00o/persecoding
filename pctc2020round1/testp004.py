x = int(input())
y = int(input())
z = int(input())

jen_area = x * z

sid_area = (y * z) / 2

if jen_area > sid_area:
    print("Jen")
    print("{:.1f}".format(jen_area - sid_area))
else:
    print("Sid")
    print("{:.1f}".format(sid_area - jen_area))
