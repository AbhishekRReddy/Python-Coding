'''
https://leetcode.com/problems/jump-game/description/
'''


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        zero_pos = []
        if nums[0] == 0:
            if len(nums) == 1:
                return True
            return False
        for i, num in enumerate(nums):
            if num == 0:
                zero_pos.append(i)
        print(zero_pos)
        for i,num in enumerate(nums):
            if num == 0:
                jump = 0
            else:
                jump = i+num
            dummy_zero = zero_pos[:]
            for z in dummy_zero:
                if jump > z and i < z:
                    zero_pos.remove(z)
        print(zero_pos)
        if len(zero_pos) == 1:
            if zero_pos[0] == len(nums)-1:
                return True
            else: 
                return False
        elif len(zero_pos) > 1:
            return False
        else:
            return True

