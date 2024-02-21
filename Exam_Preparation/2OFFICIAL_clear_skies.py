n = int(input())

matrix = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

current_position = None
armor = 300
enemies = 4

for row in range(n):
    data = list(input())
    if "J" in data:
        current_col = data.index("J")
        current_position = [row, current_col]
    matrix.append(data)

while True:
    command = input()

    if armor <= 0:
        break
    if enemies == 0:
        break
    current_row_index, current_col_index = current_position
    row_movement, col_movement = directions[command]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    if 0 <= desired_row_index < n and 0 <= desired_col_index < len(matrix[0]):
        symbol = matrix[desired_row_index][desired_col_index]
        matrix[desired_row_index][desired_col_index] = 'J'
        matrix[current_row_index][current_col_index] = '-'
        current_position = [desired_row_index, desired_col_index]

        if symbol == 'E':
            enemies -= 1
            if enemies == 0:
                print("Mission accomplished, you neutralized the aerial threat!")
                for row in matrix:
                    print(''.join(row))
                break
            else:
                armor -= 100
                if armor == 0:
                    print(f"Mission failed, your jetfighter was shot down! "
                          f"Last coordinates [{desired_row_index}, {desired_col_index}]!")
                    for row in matrix:
                        print(''.join(row))
                    break
        elif symbol == 'R':
            armor = 300
    else:
        break
