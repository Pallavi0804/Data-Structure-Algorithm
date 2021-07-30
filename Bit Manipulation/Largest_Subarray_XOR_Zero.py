def largest_subarray_length(array):
    length = 0
    xor_output = 0
    hash = {}
    for i in range(len(array)):
        xor_output = xor_output ^ array[i]
        if xor_output == 0:
            if length < i+1: length = i+1
            continue
        if xor_output not in hash:
            hash[xor_output] = i
        else:
            pre_index = hash[xor_output]
            subarray_len = i - pre_index
            if length < subarray_len:
                length = subarray_len

    return length

array = [1,2,6,5,1,2,3,5,6,7]
print(largest_subarray_length(array))
