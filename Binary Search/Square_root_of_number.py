# https://practice.geeksforgeeks.org/problems/square-root/0/?company[]=Amazon&company[]=Adobe&company[]=Google&company[]=Flipkart&company[]=Walmart&company[]=Directi&company[]=VMWare&company[]=Facebook&company[]=Linkedin&company[]=Yahoo&company[]=Media.net%20&company[]=Twitter&company[]=Apple&company[]=Zomato&company[]=Amazon&company[]=Adobe&company[]=Google&company[]=Flipkart&company[]=Walmart&company[]=Directi&company[]=VMWare&company[]=Facebook&company[]=Linkedin&company[]=Yahoo&company[]=Media.net%20&company[]=Twitter&company[]=Apple&company[]=Zomato&problemType=functional&page=1&category[]=Binary%20Search&query=company[]Amazoncompany[]Adobecompany[]Googlecompany[]Flipkartcompany[]Walmartcompany[]Directicompany[]VMWarecompany[]Facebookcompany[]Linkedincompany[]Yahoocompany[]Media.net%20company[]Twittercompany[]Applecompany[]ZomatoproblemTypefunctionalpage1company[]Amazoncompany[]Adobecompany[]Googlecompany[]Flipkartcompany[]Walmartcompany[]Directicompany[]VMWarecompany[]Facebookcompany[]Linkedincompany[]Yahoocompany[]Media.net%20company[]Twittercompany[]Applecompany[]Zomatocategory[]Binary%20Search

#https://leetcode.com/problems/sqrtx/

class Solution:
    def floorSqrt(self, x):
        low = 1
        high = x
        sqrt = 0
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                sqrt = mid
                break
            elif mid * mid < x:
                sqrt = mid
                low = mid + 1
            elif mid * mid > x:
                high = mid - 1

        return sqrt


import math
def main():
    T = int(input())
    while (T > 0):
        x = int(input())
        print(Solution().floorSqrt(x))
        T -= 1


if __name__ == "__main__":
    main()

'''
input
1
25
----
1
5
'''
