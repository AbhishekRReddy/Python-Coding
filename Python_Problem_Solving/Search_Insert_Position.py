'''
https://leetcode.com/problems/search-insert-position/description/
'''


class Solution:
    def binary_search(self, nums,target, low, high):
        if low >= high:
            if target<nums[0]:
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
        mid =(low+high)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid] and target > nums[mid-1]:
            return mid
        elif target > nums[mid] and target < nums[mid+1]:
            return mid+1
        else:
            if target < nums[mid]:
                return self.binary_search(nums,target,low,mid-1)
            else:
                return self.binary_search(nums,target,mid+1,high)

    def searchInsert(self, nums, target) -> int:
        high = len(nums)-1
        return self.binary_search(nums,target,0,high)

    