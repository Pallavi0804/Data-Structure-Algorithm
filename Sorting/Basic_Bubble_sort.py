def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

array = [5,3,8,10,36,1,0,234,100]
print(bubble_sort(array))
