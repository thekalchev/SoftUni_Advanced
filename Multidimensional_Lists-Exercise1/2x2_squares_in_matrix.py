# # row, col = [int(el) for el in input().split()]
# #
# # matrix = []
# #
# # for row_num in range(row):
# #     matrix.append([el for el in input().split()])
# #
# #
# # up_left = None
# # up_right = None
# # down_left = None
# # down_right = None
# # counter = 0
# # for row_index in range(len(matrix) - 1):
# #     for col_index in range(len(matrix[row_index]) - 1):
# #         up_left = matrix[row_index][col_index]
# #         up_right = matrix[row_index][col_index + 1]
# #         down_left = matrix[row_index + 1][col_index]
# #         down_right = matrix[row_index + 1][col_index + 1]
# #         if up_left == up_right == down_left == down_right:
# #             counter += 1
# # print(counter)
#

# rows, cols = [int(el) for el in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# equal_blocks = 0
#
# for row in range(rows - 1):
#     for col in range(cols - 1):
#         symbol = matrix[row][col]
#         if symbol == matrix[row + 1][col] and symbol == matrix[row][col + 1] and symbol == matrix[row + 1][col + 1]:
#             equal_blocks += 1
#
# print(equal_blocks)


rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

equal_blocks = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]
        valid_block = True

        for inner_row in range(row, row + 2):
            for inner_col in range(col, col + 2):
                if symbol != matrix[inner_row][inner_col]:
                    valid_block = False
                    break

            if not valid_block:
                break
        else:
            equal_blocks += 1

print(equal_blocks)
