from collections import deque

# clothes_in_box = list(map(int, input().split()))
# rack_capacity = int(input())
#
# clothes_stack = deque(clothes_in_box)
# racks_used = 0
# current_rack_sum = 0
#
# while clothes_stack:
#     current_clothing = clothes_stack.pop()
#     current_rack_sum += current_clothing
#
#     if current_rack_sum == rack_capacity:
#         current_rack_sum = 0
#         racks_used += 1
#     elif current_rack_sum > rack_capacity:
#         current_rack_sum = current_clothing
#         racks_used += 1
#
# if current_rack_sum > 0:
#     racks_used += 1
#
# print(racks_used)

clothes = [int(x) for x in input().split()]
rack_space = int(input())

racks_count = 1
current_rack_space = rack_space

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = rack_space - cloth

print(racks_count)
