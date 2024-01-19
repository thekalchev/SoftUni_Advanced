# odd_set = set()
# even_set = set()
# current_row = 0
# for name in range(int(input())):
#     current_name = input()
#     current_sum = 0
#     current_row += 1
#
#     for letter in current_name:
#         current_sum += ord(letter)
#
#     current_sum = int(current_sum / current_row)
#
#     if current_sum % 2 == 0:
#         even_set.add(current_sum)
#     else:
#         odd_set.add(current_sum)
#
# if sum(odd_set) == sum(even_set):
#     print(', '.join(map(str, (odd_set | even_set))))
# elif sum(odd_set) > sum(even_set):
#     print(', '.join(map(str, (odd_set - even_set))))
# elif sum(even_set) > sum(odd_set):
#     print(', '.join(map(str, (even_set ^ odd_set))))
#

odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(l) for l in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)
    else:
        odd_set.add(ascii_sum_of_name)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep=', ')
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
