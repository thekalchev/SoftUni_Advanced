def grocery_store(**products):
    products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    # първо по стойността (-x[1]), после по дължината на името (bread) в намалящ ред,
    # последно по името в азбучен ред (от А към Я)
    # минусът казва - сортирай в намалящ ред
    result = []

    for product, quantity in products:
        result.append(f'{product}: {quantity}')

    return '\n'.join(result)

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
