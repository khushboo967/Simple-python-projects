rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element for position ({i},{j}): "))
        row.append(value)
    matrix.append(row)

print("Multi-dimensional array:")
for row in matrix:
    print(row)