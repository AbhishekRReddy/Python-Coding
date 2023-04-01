'''
https://leetcode.com/problems/container-with-most-water/description/

'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0 #left pointer
        j =len(height)-1 #right pointer
        water = 0 #Current area of the water
        while i<j:
            water = max(water, (j-i)*min(height[i],height[j]))
            if height[i]<height[j]: 
                #we are under utilizing the height of j so search for better i
                i += 1
            elif height[i]> height[j]:
                #we under utilizing the height of i so search for better j
                j -= 1
            else:
                #if both i and j heights are equal, then this is maximum
                #volume for them. Lets reduce both of them and check
                i += 1
                j -= 1
        return water

