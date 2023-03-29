'''
https://leetcode.com/problems/first-unique-character-in-a-string/description/

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for letter in s:
            dict[letter] = dict.setdefault(letter, 0) + 1
        key_value = [(value, key) for (key, value) in dict.items()]
        key_value.sort(key = (lambda x:x[0]))
        print(key_value)
        if key_value[0][0] == 1:
            return s.find(key_value[0][1])
        return -1