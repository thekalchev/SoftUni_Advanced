from collections import deque

chocolates_count = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolates_count and milk_cups:
    chocolate = chocolates_count.pop()
    cup_of_milk = milk_cups.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        milk_cups.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates_count.append(chocolate)
        continue

    if cup_of_milk == chocolate:
        milkshakes += 1
    else:
        milk_cups.append(cup_of_milk)
        chocolates_count.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates_count) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_cups) or 'empty'}")