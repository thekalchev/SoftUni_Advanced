def is_in_scope(row_index, col_index, row_count, col_count):
    return 0 <= row_index < row_count and 0 <= col_index < col_count


direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

initial_position = None

n, m = [int(el) for el in input().split()]

matrix = []

for row_index in range(n):
    data = list(input())

    if 'B' in data:
        col_index = data.index('B')
        initial_position = (row_index, col_index)
    matrix.append(data)

current_position = initial_position

while True:
    direction = input()

    current_row_index, current_col_index = current_position
    row_movement, col_movement = direction_mapper[direction]
    desired_row = current_row_index + row_movement
    desired_col = current_col_index + col_movement

    if not is_in_scope(desired_row, desired_col, n, m):
        matrix[initial_position[0]][initial_position[1]] = ' '
        print('The delivery is late. Order is canceled.') # ако излезем от scope-a
        break

    symbol = matrix[desired_row][desired_col]

    if symbol == '*': # ако е звездичка следващия символ не местиш
        continue
    # ако не е, местиш
    current_position = [desired_row, desired_col] # променяме желаната позиция на current_position

    if symbol == 'P':
        print('Pizza is collected. 10 minutes for delivery.')
        matrix[desired_row][desired_col] = 'R' # променяме на R

    elif symbol == 'A':
        matrix[desired_row][desired_col] = 'P' # променяме на Р
        print('Pizza is delivered on time! Next order...')
        break

    elif symbol == '-':
        matrix[desired_row][desired_col] = '.' # променяме на .

for row in matrix:
    print(''.join(row))
