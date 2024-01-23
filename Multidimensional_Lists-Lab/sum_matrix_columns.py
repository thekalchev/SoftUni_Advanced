# row, col = [int(el) for el in input().split(', ')]
#
# matrix = []
#
# for i in range(row):
#     data = [int(el) for el in input().split()]
#     matrix.append(data)
#
# column_sums = [0] * col
#
# for i in range(row):
#     for j in range(col):
#         column_sums[j] += matrix[i][j]
#
# for total in column_sums:
#     print(total)

# row, col = [int(el) for el in input().split(', ')]
#
# matrix = [[int(el) for el in input().split()] for _ in range(row)]
#
# column_sums = [sum(matrix[i][j] for i in range(row)) for j in range(col)]
#
# for total in column_sums:
#     print(total)

row, col = [int(el) for el in input().split(', ')]

matrix = []
for _ in range(row):
    row_nums = [int(el) for el in input().split()]
    matrix.append(row_nums)

for col_index in range(col):
    col_total = 0
    for row_index in range(row):
        col_total += matrix[row_index][col_index]
    print(col_total)
