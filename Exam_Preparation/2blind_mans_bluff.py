N, M = map(int, input().split())
matrix = []
directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)}
touched_opponents = 0
moves = 0
current_position = None

for row in range(N):
    data = input().split()
    if "B" in data:
        current_col = data.index("B")
        current_position = [row, current_col]
    matrix.append(data)

while True:
    command = input()
    if command == "Finish" or touched_opponents == 3:
        break
    matrix[current_position[0]][current_position[1]] = '-'
    dir_row = directions[command][0] + current_position[0]
    dir_col = directions[command][1] + current_position[1]

    if 0 <= dir_row < N and 0 <= dir_col < M:
        symbol = matrix[dir_row][dir_col]

        if symbol == 'O':
            continue

        elif symbol == '-':
            moves += 1
            current_position = [dir_row, dir_col]

        elif symbol == 'P':
            matrix[dir_row][dir_col] = '-'
            current_position = [dir_row, dir_col]
            moves += 1
            touched_opponents += 1

print(f'Game over!\nTouched opponents: {touched_opponents} Moves made: {moves}')
