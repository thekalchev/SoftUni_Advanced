parentheses_sequence = input()

stack = []
opening_brackets = "({["
closing_brackets = ")}]"

for bracket in parentheses_sequence:
    if bracket in opening_brackets:
        stack.append(bracket)
    elif bracket in closing_brackets:
        if not stack or opening_brackets[closing_brackets.index(bracket)] != stack.pop():
            print("NO")
            break
else:
    print("YES" if not stack else "NO")


