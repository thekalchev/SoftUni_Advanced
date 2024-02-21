def cookbook(*args):
    recipes_by_cuisine = {}

    for recipe in args:
        name, cuisine, ingredients = recipe
        if cuisine not in recipes_by_cuisine:
            recipes_by_cuisine[cuisine] = []
        recipes_by_cuisine[cuisine].append((name, ingredients))

    sorted_cuisines = sorted(recipes_by_cuisine.keys(), key=lambda k: (-len(recipes_by_cuisine[k]), k.lower()))

    result = []

    for cuisine in sorted_cuisines:
        recipes = sorted(recipes_by_cuisine[cuisine], key=lambda r: r[0])
        result.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")

        for recipe_name, recipe_ingredients in recipes:
            result.append(f"  * {recipe_name} -> Ingredients: {', '.join(recipe_ingredients)}")

    return '\n'.join(result)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
