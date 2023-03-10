class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = nums
        length = len(a)
        current_elem = a[0]
        last_elem = a[length-1]
        counter = 1
        i = 1
        while current_elem != last_elem:
            if a[i] == a[i-1]:
                for j in range(i, length-1):
                    a[j] = a[j+1]
                continue
            current_elem = a[i]
            counter += 1
            i += 1
        return counter



sol1 = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol1.removeDuplicates(nums)
for i in range(k):
    print(nums[i])