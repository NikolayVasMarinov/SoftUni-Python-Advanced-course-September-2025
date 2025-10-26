def palindrome(word: str, index: int) -> str:

    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"

    if index == len(word) // 2:
        return f"{word} is a palindrome"

    return palindrome(word, index + 1)