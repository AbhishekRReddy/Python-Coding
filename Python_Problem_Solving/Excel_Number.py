'''
https://leetcode.com/problems/excel-sheet-column-number/description/
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_number = 0
        for letter in columnTitle:
            col_number = col_number*26 + (ord(letter)-64)
        return col_number
