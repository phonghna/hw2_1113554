# question3.py
# 湖阮英風
# 1113554
# Date of Submission: TBD

import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    for i, array in enumerate(arrays):
        if array:
            heapq.heappush(min_heap, (array[0], i, 0))

    while min_heap:
        val, array_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)

        if element_idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, array_idx, element_idx + 1))

    return result


#READ THIS: if you are lazy to type the input then comment all the lines in "input zone" and uncomment the "lazy input"

#------INPUT ZONE---------
arrays = []
k = int(input("Enter number of sorted arrays: "))
for i in range(k):
    data = list(map(int, input().split()))
    arrays.append(data)
#-----INPUT ZONE----------

#------LAZY INPUT---------
#arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#-----LAZY INPUT---------

print("\n\nMerged Array:", merge_k_sorted_arrays(arrays))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
