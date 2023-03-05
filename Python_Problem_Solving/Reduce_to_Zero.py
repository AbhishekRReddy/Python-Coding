# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
class Solution:
    def numberOfSteps(self, num):
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                steps += 1
                continue
            num -= 1
            steps += 1
        return steps

 