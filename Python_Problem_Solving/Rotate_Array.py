https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            temp = nums.pop()
            nums.insert(0,temp)
        return nums

'''
Without using the inbuilt methods
'''
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = [nums[i] for i in range(len(nums)-k,len(nums))]
        print(nums)
        for i in range(len(nums)-k-1,-1,-1):
            nums[i+k] = nums[i]
        print(nums)
        for i in range(0,k):
            nums[i] = temp[i]
        