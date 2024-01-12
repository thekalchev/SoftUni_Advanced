# from collections import deque
from collections import deque

names = deque(input().split())
number_of_tosses = int(input()) - 1

while len(names) > 1:
    names.rotate(-number_of_tosses)
    removed_kid = names.popleft()
    print(f'Removed {removed_kid}')
print(f'Last is {names.popleft()}')
