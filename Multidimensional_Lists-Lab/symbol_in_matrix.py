row = int(input())

matrix = []

for _ in range(row):
    matrix.append(list(input()))

# element_to_search = input()
# for row in range(len(matrix)):
#     for element in matrix[row]:
#         if element == element_to_search:
#             print(f'({row}, {matrix[row].index(element)})')
#             exit()
# print(f'{element_to_search} does not occur in the matrix')

searched_element = input()
is_found = False
for row_index in range(row):
    if is_found:
        break
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_element:
            print(f'({row_index}, {col_index})')
            is_found = True
            break

if not is_found:
    print(f'{searched_element} does not occur in the matrix')