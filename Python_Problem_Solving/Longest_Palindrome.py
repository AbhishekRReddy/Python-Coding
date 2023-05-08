'''
https://leetcode.com/problems/longest-palindrome/description/
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        first_odd = 0
        maxi = 0
        temp = 0
        for key,value in dict.items():
            if value % 2 == 1:
                maxi = maxi + (value - 1)
                temp = 1
            else:
                maxi += value
        return maxi + temp
        
        