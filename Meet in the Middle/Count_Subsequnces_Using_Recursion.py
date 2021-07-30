# Return Count of subsequence array where sum of subsequence is k
# Incomplete
def Count_Subsequnces_Sum(array,x):
    mid = (0 + len(array))//2
    left = array[0:mid]
    right = array[mid:len(array)]
    sum_array = []
    sum_dictionary = {}
    sum = 0
    # For left subarray
    cal(0, sum, left, x, sum_array[:],sum_dictionary)
    # For right subarray
    cal(0, sum, right, x, sum_array[:],sum_dictionary)

def cal(ind,sum,array,x,sum_array,sum_dictionary):
    if ind == len(array):
        sum_array.append(sum)
        return
    # Pick
    sum += array[ind]
    cal(ind+1,sum,array,x,sum_array,sum_dictionary)
    sum -= array[ind]
    # Non Pick
    cal(ind+1,sum,array,x,sum_array,sum_dictionary)
    print(sum_array)

array = [1,2,3,2]
x = 5
Count_Subsequnces_Sum(array,x)
