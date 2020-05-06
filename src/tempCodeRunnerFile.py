0
print(matrix[0][1])  # 20
for row in matrix:
    for num in row:
        print(num)
print(matrix2)

uniques = set()
for row in matrix:
    for num in row:
        uniques.add(num)
print(uniques)
