"""
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
"""

class Solution:
    def matrixBlockSum(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        # Create prefix sum matrix and initialize it with 0 . we use n+1 so that we get extra row and column to make calculationo much easier
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        # print(prefix)
        
        #add the sum and insert it into the i,j position in radius of k
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                top = max(0, i - k)
                bottom = min(m - 1, i + k)

                left = max(0, j - k)
                right = min(n - 1, j + k)

                answer[i][j] = (
                    prefix[bottom + 1][right + 1]
                    - prefix[top][right + 1]
                    - prefix[bottom + 1][left]
                    + prefix[top][left]
                )

        return answer
    
    
s=Solution()
s.matrixBlockSum( mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1)