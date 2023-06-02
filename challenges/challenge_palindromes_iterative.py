def is_palindrome_iterative(word):
    if word is None or len(word) == 0:
        return False

    reversed_word = word[::-1]

    if reversed_word.lower() == word.lower():
        return True
    return False
