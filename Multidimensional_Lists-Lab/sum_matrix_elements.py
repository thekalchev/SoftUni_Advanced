row, col = [int(el) for el in input().split(', ')]

total_amount = 0
matrix = []
for i in range(row):
    data = [int(el) for el in input().split(', ')]
    total_amount += sum(data)
    matrix.append(data)

print(total_amount)
print(matrix)