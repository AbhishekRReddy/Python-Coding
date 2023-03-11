'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_parent = len(haystack)
        length_child = len(needle)
        i = 0
        j = length_child
        while True:
            temp_i = i
            temp_j = j
            while temp_j <= length_parent:
                if haystack[temp_i:temp_j] == needle:
                    return temp_i
                temp_i += 1
                temp_j += 1
            i += 1
            j += 1
            if j >=length_parent:
                return -1



