def min_subarray_len(target, nums):

    left = 0
    total = 0
    answer = float('inf')

    for right in range(len(nums)):

        total += nums[right]

        while total >= target:

            answer = min(
                answer,
                right-left+1
            )

            total -= nums[left]
            left += 1

    return 0 if answer == float('inf') else answer


print(min_subarray_len(7,[2,3,1,2,4,3]))
