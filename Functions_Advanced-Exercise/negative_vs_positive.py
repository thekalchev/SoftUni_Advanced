# nums = [int(x) for x in input().split()]
#
# positive = [x for x in nums if x >= 0]
# negative = [x for x in nums if x < 0]
#
# positive_sum = sum(positive)
# negative_sum = sum(negative)
#
# print(negative_sum)
# print(positive_sum)
#
# if abs(positive_sum) < abs(negative_sum):
#     print('The negatives are stronger than the positives')
# else:
#     print(f'The positives are stronger than the negatives')
#
def print_numbers(nums):
    positive_sum = sum(num for num in nums if num > 0)
    negative_sum = sum(num for num in nums if num < 0)

    print(negative_sum)
    print(positive_sum)

    if positive_sum > abs(negative_sum):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')


numbers = [int(x) for x in input().split()]
print_numbers(numbers)
