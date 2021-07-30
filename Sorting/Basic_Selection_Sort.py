def selection_sort(array):
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                array[i],array[j] = array[j],array[i]
    return array

array = [5,3,8,10,36,1,0,234,100]
print(selection_sort(array))
