def can_jump(nums):

    reachable = 0

    for i in range(len(nums)):

        if i > reachable:
            return False

        reachable = max(
            reachable,
            i + nums[i]
        )

    return True


print(can_jump([2,3,1,1,4]))
