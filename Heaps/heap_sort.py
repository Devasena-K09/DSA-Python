import heapq

def heap_sort(nums):

    heapq.heapify(nums)

    result = []

    while nums:
        result.append(heapq.heappop(nums))

    return result


print(heap_sort([4,1,7,3,8]))
