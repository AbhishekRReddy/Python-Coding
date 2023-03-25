'''
https://leetcode.com/problems/pascals-triangle/
'''
#Intersting problem, the key here is to understand the logic behid the pascals triangle
#Each row is power to 11
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []
        for row in range(numRows):
            new_row = str(11**row)
            new_row = [int(x) for x in new_row]
            pascals_triangle.append(new_row)
        print(pascals_triangle)
        return pascals_triangle

   