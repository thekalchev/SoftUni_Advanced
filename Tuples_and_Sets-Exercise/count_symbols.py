# occurences = {}
#
# for symbol in input():
#     occurences[symbol] = occurences.get(symbol, 0) + 1
#
# for symbol, times in sorted(occurences.items()):
#     print(f'{symbol}: {times} time/s')

text = input()

for symbol in sorted(set(text)):
    print(f'{symbol}: {text.count(symbol)} time/s')

