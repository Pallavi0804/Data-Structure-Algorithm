class Solution:
    def merge_two_sorted_array(self,a,b):
        m1 = min(len(a),len(b))
        a_index = 0
        b_index = 0
        sorted = []
        for i in range(m1):
            if a[a_index] < b[b_index]:
                sorted.append(a[a_index])
                a_index += 1
            else:
                sorted.append(b[b_index])
                b_index += 1

        if a_index == len(a) - 1:
            sorted.append(a[a_index])
        if b_index == len(b) - 1:
            sorted.append(b[b_index])

        if a_index-1 != len(a):
            for ind in range(a_index,len(a)):
                sorted.append(a[ind])

        if b_index-1 != len(b):
            for ind in range(b_index,len(b)):
                sorted.append(b[ind])

        return sorted


s = Solution()
a = [1,10,15,20]
b = [5,6,15]
print(s.merge_two_sorted_array(a,b))
