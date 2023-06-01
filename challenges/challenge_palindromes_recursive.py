def is_palindrome_recursive(word, low_index, high_index):
    if word == "" or low_index is None or high_index is None:
        return False

    if low_index > high_index:
        return True
    if word[low_index].lower() != word[high_index].lower():
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
