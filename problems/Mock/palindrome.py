def is_palindrome(word: str) -> bool:
    low, high = 0, len(word) - 1

    while low < high:
        if word[low] != word[high]:
            return False

        low += 1
        high -= 1

    return True


print(is_palindrome('anora'))
