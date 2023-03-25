'''
https://leetcode.com/problems/pascals-triangle/
'''
#Intersting problem, the key here is to understand the logic behid the pascals triangle
#Each row is power to 11
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascals_triangle = []
        for row in range(numRows):
            new_row = str(11**row)
            new_row = [int(x) for x in new_row]
            pascals_triangle.append(new_row)
        print(pascals_triangle)
        return pascals_triangle

#The above code works only till the 5 rows. But to get more than that, we need implement like following
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascals_triangle = [[1]]
        for _ in range(1, numRows):
            temp = [0] + pascals_triangle[-1] + [0]
            new_row = []
            for j in range(len(temp)-1):
                new_row.append(temp[j] + temp[j+1])
            pascals_triangle.append(new_row)
        return pascals_triangle