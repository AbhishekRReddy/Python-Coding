'''
https://leetcode.com/problems/plus-one/description/
'''
class Solution:
    def plusOne(self, digits):
        digits = [str(x) for x in digits]
        num = int(''.join(digits))
        num += 1
        num = str(num).strip()
        digits=[]
        for x in num:
            digits.append(int(x.strip()))
        return (digits)

                    




