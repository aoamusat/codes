from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    count = 0
    for i in nums:
        if i == 0:
            count += 1
    j = 0
    for i in nums:
        if i != 0:
            nums[j] = i
            j += 1
    while j < n and count:
        nums[j] = 0
        count -= 1
        j += 1 
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))