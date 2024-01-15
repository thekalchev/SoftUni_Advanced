# stack = []
# n_lines = int(input())
# for line in range(n_lines):
#     query = input().split()
#     command = query[0]
#     if command == '1':
#         number = int(query[1])
#         stack.append(number)
#     elif command == '2':
#         if stack:
#             stack.pop()
#     elif command == '3':
#         if stack:
#             print(max(stack))
#     elif command == '4':
#         if stack:
#             print(min(stack))
# print(', '.join(map(str, reversed(stack))))

# ========================================================================

# numbers = []
#
# for _ in range(int(input())):
#     numbers_data = [int(x) for x in input().split()]
#     command = numbers_data[0]
#     if command == 1:
#         numbers.append(numbers_data[1])
#     elif command == 2:
#         if numbers:
#             numbers.pop()
#     elif command == 3:
#         if numbers:
#             print(max(numbers))
#     elif command == 4:
#         if numbers:
#             print(min(numbers))
#
# numbers.reverse()
# print(*numbers, sep=', ')

# ================================================================================
# def append(x: list):
#     numbers.append(x[1]) така би изглеждала ламбда функцията за апенд


numbers = []

map_functions = {
    '1': lambda x: numbers.append(x[1]),
    '2': lambda x: numbers.pop() if numbers else None,
    '3': lambda x: print(max(numbers)) if numbers else None,
    '4': lambda x: print(min(numbers)) if numbers else None
}

for _ in range(int(input())):
    numbers_data = input().split()
    command = numbers_data[0]
    map_functions[command](numbers_data) #ключ - командата

numbers.reverse()
print(*numbers, sep=', ')
