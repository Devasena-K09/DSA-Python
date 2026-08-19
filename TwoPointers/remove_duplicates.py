def remove_duplicates(nums):

    if not nums:
        return 0

    left = 1

    for right in range(1, len(nums)):

        if nums[right] != nums[right - 1]:

            nums[left] = nums[right]
            left += 1

    return left


nums = [1,1,2,2,3]

print(remove_duplicates(nums))
