# nums = list(map(int, input().split()))
# set1 = set()
# set2 = set()
# for i in range(nums[0]):
#     num = int(input())
#     set1.add(num)
# for i in range(nums[1]):
#     num = int(input())
#     set2.add(num)
# print(*set1.intersection(set2), sep='\n')
#

n, m = [int(x) for x in input().split()]

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print(*first_set.intersection(second_set), sep='\n')