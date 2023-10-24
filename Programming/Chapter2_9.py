a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
index = sorted([a, b, c])
a, b, c = str(index[0]), str(index[1]), str(index[2])
result = a + '->' + b + '->' + c
print(result)
