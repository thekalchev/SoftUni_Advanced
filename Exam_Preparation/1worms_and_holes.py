from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

matches = 0
all_worms_count = len(worms)

while worms and holes:
    last_worm = worms[-1]
    first_hole = holes[0]

    if last_worm == first_hole:
        worms.pop()
        holes.popleft()
        matches += 1
    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matches:
    print(f'Matches: {matches}')
else:
    print(f'There are no matches.')

if not worms and matches == all_worms_count:
    print(f'Every worm found a suitable hole!')
elif not worms and matches < all_worms_count:
    print('Worms left: none')
else:
    print(f'Worms left: {", ".join([str(el) for el in worms])}')

if not holes:
    print(f'Holes left: none')

if holes:
    print(f'Holes left: {", ".join([str(el) for el in holes])}')
