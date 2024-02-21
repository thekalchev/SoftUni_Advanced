# matrix = []
#
# for row in range(int(input())):
#     matrix.append([int(el) for el in input().split()])
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
#
# difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
# print(difference)



# num = int(input())
# matrix = [[int(el) for el in input().split()] for _ in range(num)]
#
# primary_sum, secondary_sum = 0, 0
#
# for i in range(num):
#     primary_sum += matrix[i][i]
#     secondary_sum += matrix[i][num - i - 1]
#
# print(abs(primary_sum - secondary_sum))



num = int(input())

primary_sum, secondary_sum = 0, 0

for i in range(num):
    line = [int(x) for x in input().split()]
    primary_sum += line[i]
    secondary_sum += line[num - i - 1]

print(abs(primary_sum - secondary_sum))
