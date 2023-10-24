amount = int(input())
if amount < 0:
    print("Invalid Value!")
elif amount <= 50:
    expense = 0.53 * amount
    print("cost = {0:.2f}".format(expense))
else:
    expense = 26.5 + (amount - 50) * 0.58
    print("cost = {0:.2f}".format(expense))
