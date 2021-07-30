def linear_search(arr_linear,search_ele):
    flag =''
    for i in range(len(arr_linear)):
        if search_ele == arr_linear[i]:
            flag = "Found Element"
            break
    else:
        flag = "Element not found"

    return flag

def binary_search(arr_binary,search_ele):
    flag = ''
    low  = 0
    high = len(arr_binary)-1
    while low <= high:
        mid = (low + high) // 2
        if arr_binary[mid] == search_ele:
            flag ="Element Found"
            break
        elif search_ele > arr_binary[mid]:
            low = mid + 1
        elif search_ele < arr_binary[mid]:
            high = mid -1
    else:
        flag = "Element Not Found"

    return flag


search_ele = 1
arr_linear = [1,5,4,3,4,2,1]
print(linear_search(arr_linear,search_ele))
arr_binary = [1,3,5,6,6,7,8,9,10]
print(binary_search(arr_binary,search_ele))
