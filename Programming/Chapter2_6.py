N = int(input())
sum = 0
for i in range(1, N + 1):
    but = (2 * i - 1)
    top = i
    sign = (-1)**(i-1)
    sum = sum + sign * top / but
print("{0:.3f}".format(sum))
