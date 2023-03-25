'''
https://leetcode.com/problems/missing-number/description/
'''
'''
1. Find the sum upto n natural number by using the formula: n*(n+1)/2
2. Find the sum of the given array.
3. Difference between above two sums is the missing number. 
4. If both sums are missing, the zero is missing from the given list.

'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        theor_sum = l*(l+1)//2
        actual_sum = sum(nums)
        if actual_sum == theor_sum:
            return 0
        return theor_sum - actual_sum