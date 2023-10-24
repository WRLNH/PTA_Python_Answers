m, n = input().split()
m, n = int(m), int(n)
sum = 0.0
for i in range(m, n + 1):
    sum = sum + i * i + 1 / (i)
print("sum = {0:.6f}".format(sum))
