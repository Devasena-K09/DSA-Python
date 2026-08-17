def max_subarray(nums):
    current = maximum = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        maximum = max(maximum, current)

    return maximum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
