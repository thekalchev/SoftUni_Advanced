from collections import deque

# string = input().split()
# while string:
#     print(string.pop(), end = ' ')


# numbers = deque(input().split())
# for _ in range(len(numbers)):
#     print(numbers.pop(), end=' ')

numbers = deque(input().split())
numbers.reverse()
print(*numbers)