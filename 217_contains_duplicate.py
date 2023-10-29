from typing import List


nums = [1, 2, 3, 4, 5]


def contains_duplicate(nums: List[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False


print(contains_duplicate(nums))
