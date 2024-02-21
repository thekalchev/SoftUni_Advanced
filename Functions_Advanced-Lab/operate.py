from functools import reduce  # в reduce елементите излизат 2 по 2


def operate(operator, *args):
    if operator == '+':
        return reduce(lambda x, y: x + y, args)
    elif operator == '-':
        return reduce(lambda x, y: x - y, args)
    elif operator == '*':
        return reduce(lambda x, y: x * y, args)
    elif operator == '/':
        return reduce(lambda x, y: x / y, args)

    #return reduce(lambda x,y: eval(f'{x}{operator}{y}'), args)

print(operate("-", 10, 4))
