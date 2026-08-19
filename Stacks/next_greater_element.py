def next_greater_element(nums):

    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)-1, -1, -1):

        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result


nums = [4, 5, 2, 25]

print(next_greater_element(nums))
