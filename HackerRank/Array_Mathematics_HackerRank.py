import numpy as np

first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])

a_rows = []
for i in range(n):
    row = input().split()
    row = list(map(int, row))
    a_rows.append(row)

b_rows = []
for i in range(n):
    row = input().split()
    row = list(map(int, row))
    b_rows.append(row)

a = np.array(a_rows, int)
b = np.array(b_rows, int)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
