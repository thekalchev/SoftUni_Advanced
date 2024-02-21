from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < cols:  # rows = 3, cols = 6, word = 'so'
        word_copy.extend(word)  # word_copy = sososo

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep='')
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep='')

#softuni len - po- golqmo ot 6, printirame i ostava poslednata bukva v deka "i"
#len-a e 1, toest po-malko ot 6, znachi extendvame s word_copy i stava isoftuni
#isoftuni e po-golqmo ot 6, row-a e cheten i printirame naobratno - isoftun i tn