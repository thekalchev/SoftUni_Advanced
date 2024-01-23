# matrix = []
# for i in range(int(input())):
#     data = [int(el) for el in input().split(', ')]
#     matrix.append(data)
# matlist= []
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matlist.append(matrix[i][j])
# print(matlist)
#

# row = int(input())
#
# matrix = []
# for i in range(row):
#     row_data = [int(el) for el in input().split(', ')]
#     matrix.append(row_data)
# flattening_matrix = []
# for row in matrix:
#     for element in row:
#         flattening_matrix.append(element)
# print(flattening_matrix)

# row = int(input())
#
# matrix = []
# for i in range(row):
#     row_data = [int(el) for el in input().split(', ')]
#     matrix.append(row_data)
# flatten = [el for row in matrix for el in row]
# print(flatten)

row = int(input())

flatten = []
for i in range(row):
    row_data = [int(el) for el in input().split(', ')]
    flatten.extend(row_data)
print(flatten)