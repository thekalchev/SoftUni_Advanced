# matrix = []
#
# for row in range(int(input())):
#     matrix.append([int(el) for el in input().split(', ')])
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         if row == col:
#             primary_diagonal.append(matrix[row][col])
#
# for row in range(len(matrix)):
#     secondary_diagonal.append(matrix[row][len(matrix) - row - 1])
#
# print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
# print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')

n = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
second = [matrix[r][n-r-1] for r in range(n)]

print(f'Primary diagonal: {", ".join(map(str, primary))}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(map(str, second))}. Sum: {sum(second)}')

