'''
https://leetcode.com/problems/two-sum/description/

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i,elem1 in enumerate(nums):
            for j,elem2 in enumerate(nums):
                if i == j:
                    continue
                if(elem1+elem2 == target):
                    output.append(i)
                    output.append(j)
                    return output
                    