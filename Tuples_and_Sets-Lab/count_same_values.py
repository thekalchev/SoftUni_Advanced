# numbers = tuple(float(x) for x in input().split())
# original_numbers = []
# for number in numbers:
#     if number not in original_numbers:
#         original_numbers.append(number)
# for num in original_numbers:
#     print(f'{num} - {numbers.count(num)} times')

numbers = tuple(float(x) for x in input().split())

same_values = {}

for num in numbers:
    if num not in same_values:
        same_values[num] = numbers.count(num)
for number, occ in same_values.items():
    print(f'{number} - {occ} times')