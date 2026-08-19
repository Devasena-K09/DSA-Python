def max_area(height):

    left = 0
    right = len(height) - 1

    answer = 0

    while left < right:

        area = min(
            height[left],
            height[right]
        ) * (right - left)

        answer = max(answer, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return answer


print(max_area([1,8,6,2,5,4,8,3,7]))
