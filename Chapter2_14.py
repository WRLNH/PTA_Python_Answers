A, B = input().split()
A, B = int(A), int(B)
j = 0
sum = 0
for i in range(A, B + 1):
    j = j + 1
    sum = sum + i
    if j%5 !=0:
        print("{0:>5}".format(i), end = "")
    else:
        print("{0:>5}".format(i))
if j%5 !=0:
    print("\nSum =", sum)
else:
    print("Sum =", sum)