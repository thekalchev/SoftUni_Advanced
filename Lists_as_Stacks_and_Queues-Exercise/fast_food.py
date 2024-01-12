from collections import deque

quantity_of_food = int(input())
food_in_each_order = deque(map(int, input().split()))
print(max(food_in_each_order))

while quantity_of_food > 0 and food_in_each_order:
    order = food_in_each_order[0]

    if quantity_of_food >= order:
        quantity_of_food -= order
        food_in_each_order.popleft()
    else:
        break

orders_left = ' '.join(map(str,food_in_each_order))

if food_in_each_order:
    print(f'Orders left: {orders_left}')
else:
    print(f'Orders complete')
