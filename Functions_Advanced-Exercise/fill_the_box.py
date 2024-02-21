# def fill_the_box(height, length, width, *cubes):
#     volume = height * length * width
#     total_cubes = 0
#     for cube in cubes:
#         if cube == 'Finish':
#             break
#         total_cubes += cube
#         volume -= cube
#     if volume <= 0:
#         return f"No more free space! You have {abs(volume)} more cubes."
#     else:
#         return f"There is free space in the box. You could put {volume} more cubes."
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

from collections import deque

def fill_the_box(height, length, width, *cubes):
    space = length * width * height
    cubes = deque(cubes)

    while cubes[0] != 'Finish':
        space -= cubes.popleft()

        if space < 0:
            cubes_left = sum(c for c in cubes if c != 'Finish')
            return f'No more free space! You have {cubes_left + abs(space)} more cubes.'
    return f'There is free space in the box. You could put {space} more cubes.'