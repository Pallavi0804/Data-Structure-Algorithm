# https://practice.geeksforgeeks.org/problems/find-the-highest-number2259/1/?company[]=Amazon&company[]=Adobe&company[]=Google&company[]=Flipkart&company[]=Walmart&company[]=Directi&company[]=VMWare&company[]=Facebook&company[]=Linkedin&company[]=Yahoo&company[]=Media.net%20&company[]=Twitter&company[]=Apple&company[]=Zomato&company[]=Amazon&company[]=Adobe&company[]=Google&company[]=Flipkart&company[]=Walmart&company[]=Directi&company[]=VMWare&company[]=Facebook&company[]=Linkedin&company[]=Yahoo&company[]=Media.net%20&company[]=Twitter&company[]=Apple&company[]=Zomato&problemType=functional&page=1&category[]=Binary%20Search&query=company[]Amazoncompany[]Adobecompany[]Googlecompany[]Flipkartcompany[]Walmartcompany[]Directicompany[]VMWarecompany[]Facebookcompany[]Linkedincompany[]Yahoocompany[]Media.net%20company[]Twittercompany[]Applecompany[]ZomatoproblemTypefunctionalpage1company[]Amazoncompany[]Adobecompany[]Googlecompany[]Flipkartcompany[]Walmartcompany[]Directicompany[]VMWarecompany[]Facebookcompany[]Linkedincompany[]Yahoocompany[]Media.net%20company[]Twittercompany[]Applecompany[]Zomatocategory[]Binary%20Search

class Solution:
    def findPeakElement(self,a):
        low = 0
        high = len(a) - 1
        while low <= high:
            mid = (low + high) // 2
            if a[high] > a[mid]:
                return a[high]
            elif a[mid] > a[mid - 1] and a[mid] > a[mid + 1]:
                return a[mid]
            else:
                if a[mid] < a[mid + 1]:
                    low = mid + 1
                elif a[mid] < a[mid - 1]:
                    high = mid - 1
        return -1


T=int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    ob = Solution();
    ans = ob.findPeakElement(a)
    print(ans)

'''
input
1
11
1 2 3 4 5 6 5 4 3 2 1
------------
1
5
1 2 3 4 5
------------
1
11
1 2 3 4 5 6 7 8 3 2 1
'''
