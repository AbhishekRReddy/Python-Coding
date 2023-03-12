'''
https://leetcode.com/problems/majority-element/description/
'''
class Solution:
    def majorityElement(self, nums) -> int:
        dict ={}
        for i,elem in enumerate(nums):
            dict.setdefault(elem,0)
            dict[elem] += 1
        temp = [(value,key) for key,value in dict.items()]
        return max(temp)[1]
