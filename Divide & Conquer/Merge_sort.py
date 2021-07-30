# Merge sort
def merge_sort(array,low,high):
    if low == high: return
    mid = (low+high)//2
    # Left subarray
    merge_sort(array,low,mid)
    # Right subaaray
    merge_sort(array,mid+1,high)

    # merging two subarray
    array = merge(array,low,mid,high)
    return array


def merge(array,low,mid,high):
    left_i = low
    right_i = mid+1
    sorted = []
    while left_i <= mid and right_i <= high:
        if array[left_i] <= array[right_i]:
            sorted.append(array[left_i])
            left_i += 1
        else:
            sorted.append(array[right_i])
            right_i += 1

    while left_i <= mid:
        sorted.append(array[left_i])
        left_i += 1
    while right_i <= high:
        sorted.append(array[right_i])
        right_i += 1
    array[low:high+1] = sorted[:]

    return array


array = [7,6,5,3,4,1]
print(merge_sort(array,0,len(array)-1))
