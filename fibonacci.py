n = 10
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    next_val = a + b
    a = b
    b = next_val
