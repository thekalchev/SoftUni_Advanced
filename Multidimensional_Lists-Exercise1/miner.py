n = int(input())
commands = input().split()

matrix = []
miner_pos = []  # [miner_row, miner_col]
collected_coal, total_coal = 0, 0

directions = { # up ->  5, 3 -> 5 + (-1), 3 + 0 -> 4, 3
    'up': [-1, 0], # [row, col]
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

for row in range(n):
    matrix.append(input().split())

    if 's' in matrix[row]: # . . S . *  c  # с row, matrix[row].index('s') разбираме кой ред и коя колона е
        miner_pos = [row, matrix[row].index('s')] # тук е позицията на миньора
        matrix[miner_pos[0]][miner_pos[1]] = '*' # от горния ред взимаме двете и го правим на звездичка

    total_coal += matrix[row].count('c') # колко пъти има 'с' на реда

for command in commands: # command => down # directions[command] връща [1,0]
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]
    #row, col = miner_pos[0] (тоест роу) плюс роу от дирекшанс за движение, miner_pos[1] (тоест колони + колоната от дирекшанс за движение)
    if not (0 <= r < n and 0 <= c < n):
         continue

    miner_pos = [r,c] #актуализираме позицията на миньора, понеже е валидна

    if matrix[r][c] == 'c':
        collected_coal += 1

        if collected_coal == total_coal:
            print(f'You collected all coal! ({r}, {c})')
            break

    elif matrix[r][c] == 'e':
        print(f'Game over! ({r}, {c})')
        break

    matrix[r][c] = '*'

else:
    print(f'{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})')



