# highest_length = 0
# inter = list()
# for _ in range(int(input())):
#     set1 = set()
#     set2 = set()
#     first, second = input().split('-')
#     start1, end1 = first.split(',')
#     start2, end2 = second.split(',')
#     for _ in range(int(start1), int(end1) + 1):
#         set1.add(_)
#     for _ in range(int(start2), int(end2) + 1):
#         set2.add(_)
#     intersection = set1.intersection(set2)
#     if len(intersection) > highest_length:
#         highest_length = len(intersection)
#         inter = set1.intersection(set2)
#
# print(f'Longest intersection is {list(inter)} with length {highest_length}')

longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [el.split(',') for el in input().split('-')]

    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is [{", ".join(str(x) for x in longest_intersection)}]'
      f' with length {len(longest_intersection)}')
