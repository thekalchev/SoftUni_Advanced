def palindrome(word: str, idx: int):
    if idx == len(word) // 2:
        return f'{word} is a palindrome'

    if word[idx] != word[-idx - 1]:  # 0 & -1; 1 & -2; 2 & -3
        return f'{word} is not a palindrome'

    result = palindrome(word, idx + 1)
    return result

print(palindrome("abcba", 0))

