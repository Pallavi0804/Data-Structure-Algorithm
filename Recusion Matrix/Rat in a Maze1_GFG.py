# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
# 4 Directions Question (L,R,D,U)

class Solution:
    def findPath(self, m, n):
        self.matrix = m
        self.n = n
        self.paths = []
        self.p = ""
        self.hash = [[0]*n for _ in range(n)]
        return self.ratInMaze(0,0,self.paths[:],self.hash,self.p)


    def ratInMaze(self,i,j,paths,hash,p):
        # Check for invalid conditions
       if i>=self.n or j>=self.n or i<0 or j<0 or self.hash[i][j]==1 or self.matrix[i][j]==0:
           return
       if i == self.n-1 and j == self.n-1:
           self.paths.append(p)
           return

       # Mark visited element
       self.hash[i][j] = 1

       # Up
       self.ratInMaze(i - 1, j, self.paths, self.hash, p + 'U')
       # Down
       self.ratInMaze(i + 1, j, self.paths, self.hash, p + 'D')
       # Left
       self.ratInMaze(i, j - 1, self.paths, self.hash, p + 'L')
       # Right
       self.ratInMaze(i, j + 1, self.paths, self.hash, p + 'R')

       # Backtrack
       self.hash[i][j] = 0
       return self.paths


# m = [
#    [1,0,1,1,0],
#    [1,0,1,1,1],
#    [1,1,1,0,1],
#    [1,1,0,0,1],
#    [1,1,0,0,1]
# ]
# n = 5
# s = Solution()
# print(s.findPath(m,n))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        matrix = [[0 for i in range(n[0])] for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        if len(result) == 0:
            print(-1)
        else:
            for x in result:
                print(x, end=" ")
            print()
'''
input
1
4
1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1
-------
1
5
1 0 1 1 0 1 0 1 1 1 1 1 1 0 1 1 1 0 0 1 1 1 0 0 1
'''
