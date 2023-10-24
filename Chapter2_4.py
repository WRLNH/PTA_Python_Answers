a, n = input().split()
n = int(n)
s = 0
for i in range(1, n + 1):
    s = s + int(a * i)
print("s =", s)