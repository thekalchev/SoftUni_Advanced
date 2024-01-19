# lines = int(input())
# unique_elements = set()
# for _ in range(lines):
#     element = input().split()
#     if len(element) == 1:
#         unique_elements.add(*element)
#     else:
#         for _ in range(len(element)):
#             unique_elements.add(element[_])
#
#
# print(*unique_elements, sep='\n')
#


# table = set()
#
# for _ in range(int(input())):
#     for el in input().split():  # input().split -> ['Ce', 'O', 'H']
#         table.add(el)
#
# print(*table, sep='\n')


print(*{el for _ in range(int(input())) for el in input().split()}, sep='\n')