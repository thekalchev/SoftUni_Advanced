sequence = list(map(int, input().split()))
target_number = int(input())

seen_numbers = set()

for num in sequence:
    complement = target_number - num

    if complement in seen_numbers:
        print(f"{complement} + {num} = {target_number}")

    seen_numbers.add(num)
