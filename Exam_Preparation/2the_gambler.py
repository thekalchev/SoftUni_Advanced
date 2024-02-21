direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

def get_next_position(position, direction_mapper, direction, matrix):
    current_row_index, current_col_index = position
    row_movement, col_movement = direction_mapper[direction]  # 1, 0 = direction_mapper['down']
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    if 0 <= desired_row_index < len(matrix) and 0 <= desired_col_index < len(matrix):
        return desired_row_index, desired_col_index
    else:
        cash_amount = 0
        print('Game over! You lost everything!')
        exit()


size = int(input())

matrix = []
position = None
cash_amount = 100

for row_index in range(size):
    data = list(input())

    if "G" in data:  # ако S е в реда
        current_col = data.index('G')
        position = [row_index, current_col]
    matrix.append(data)

command = input()
while command != 'end':
    current_row_index, current_col_index = position
    next_row_index, next_col_index = get_next_position(position, direction_mapper, command, matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = 'G'
    matrix[current_row_index][current_col_index] = '-'
    position = [next_row_index, next_col_index]

    if cash_amount <= 0:
        print(f'Game over! You lost everything!')
        exit()

    if symbol == 'W':
        cash_amount += 100
    elif symbol == 'P':
        cash_amount -= 200
    elif symbol == 'J':
        cash_amount += 100000
        print(f'You win the Jackpot!\nEnd of the game. Total amount: {cash_amount}$')
        for row in matrix:
            print(f"{''.join(row)}")
        exit()

    command = input()

if cash_amount <= 0:
    print(f'Game over! You los'
          f't everything!')
    exit()
print(f'End of the game. Total amount: {cash_amount}$')
for row in matrix:
    print(f"{''.join(row)}")

