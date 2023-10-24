lower, upper = input().split()
lower, upper = int(lower), int(upper)
if lower > upper:
    print("Invalid.")
else:
    print("fahr celsius")
    for i in range(lower, upper + 1, 2):
        F = float(i)
        C = round(5 * (F - 32) / 9, 1)
        C_str = str(C)
        print("{0:.0f}{1:>6}".format(F, C_str))
