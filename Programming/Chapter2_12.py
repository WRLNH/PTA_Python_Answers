import math
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
array = sorted([a, b, c])
if (array[0] + array[1] <= array[2]):
    print("These sides do not correspond to a valid triangle")
else:
    a, b, c = float(array[0]), float(array[1]), float(array[2])
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    print("area = {0:.2f}; perimeter = {1:.2f}".format(area, perimeter))
