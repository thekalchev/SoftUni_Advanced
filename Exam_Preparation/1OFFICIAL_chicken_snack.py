from collections import deque

amount_of_money = deque([int(x) for x in input().split()])
prices_of_foods = deque([int(x) for x in input().split()])
foods_eaten = 0

while amount_of_money and prices_of_foods:
    last_money = amount_of_money[-1]
    first_food = prices_of_foods[0]

    if last_money == first_food:
        foods_eaten += 1
        amount_of_money.pop()
        prices_of_foods.popleft()

    elif last_money > first_food:
        difference = last_money - first_food
        foods_eaten += 1
        amount_of_money.pop()
        prices_of_foods.popleft()

        # Check if amount_of_money is not empty before accessing its last element
        if amount_of_money:
            amount_of_money[-1] += difference

    elif last_money < first_food:
        amount_of_money.pop()
        prices_of_foods.popleft()

if foods_eaten >= 4:
    print(f'Gluttony of the day! Henry ate {foods_eaten} foods.')
elif foods_eaten > 0:
    if foods_eaten > 1:
        print(f'Henry ate: {foods_eaten} foods.')
    elif foods_eaten == 1:
        print(f'Henry ate: {foods_eaten} food.')
elif foods_eaten == 0:
    print(f'Henry remained hungry. He will try next weekend again.')