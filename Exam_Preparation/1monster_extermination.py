from collections import deque

armor_of_monsters = deque([int(x) for x in input().split(',')])
striking_impact = [int(x) for x in input().split(',')]

monsters_killed = 0

while armor_of_monsters and striking_impact:

    first_monster_armor = armor_of_monsters.popleft()
    impact = striking_impact.pop()

    if impact >= first_monster_armor:
        monsters_killed += 1
        impact -= first_monster_armor
        if striking_impact:
            striking_impact[-1] += impact
        elif not striking_impact and impact > 0:
            striking_impact.append(impact)
    else:
        first_monster_armor -= impact
        armor_of_monsters.append(first_monster_armor)

if not armor_of_monsters:
    print("All monsters have been killed!")
if not striking_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {monsters_killed}")

