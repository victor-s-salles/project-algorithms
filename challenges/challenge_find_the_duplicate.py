def find_duplicate(nums):
    nums_sorted = sorted(nums)
    try:
        for n in range(len(nums_sorted) - 1):
            if nums_sorted[n] == nums_sorted[n + 1] and nums_sorted[n] >= 1:
                return nums_sorted[n]
        return False
    except TypeError:
        return False
