from collections import deque

current_materials = [int(x) for x in input().split()]
levels_of_magic = deque(int(x) for x in input().split())
crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while current_materials and levels_of_magic:
    material = current_materials.pop() if levels_of_magic[0] or not current_materials[-1] else 0  # 0
    magic_level = levels_of_magic.popleft() if material or not levels_of_magic[0] else 0  # 0
    if not magic_level:
        continue
    product = material * magic_level
    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        current_materials.append(material + magic_level)
    elif product > 0:
        current_materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if current_materials:
    print(f"Materials left: {', '.join(str(x) for x in current_materials[::-1])}")
if levels_of_magic:
    print(f"Magic left: {', '.join(str(x) for x in levels_of_magic)}")
[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]