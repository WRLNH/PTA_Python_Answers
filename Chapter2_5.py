N = int(input())
sum = 0
for i in range(1, N + 1):
    base = (2 * i - 1)
    sum = sum + 1 / base
print("sum = {0:.6f}".format(sum))