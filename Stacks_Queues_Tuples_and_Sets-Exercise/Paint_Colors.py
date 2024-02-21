from collections import deque

words = deque(input().split())
final_result = []
colors = {"red", "yellow", "blue", "purple", "orange", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ""
    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            final_result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                words.insert(len(words) // 2, el)

for color in set(req_colors.keys()).intersection(final_result):
    if not req_colors[color].issubset(final_result):
        final_result.remove(color)

print(final_result)