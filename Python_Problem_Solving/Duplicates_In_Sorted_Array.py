class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = nums
        l = len(a)
        current_elem = a[0]
        last_elem = a[l-1]
        insert_pos = 1
        for i in range(1, l):
            if current_elem == a[i]:
                continue
            a[insert_pos] = a[i]
            current_elem = a[i]
            if current_elem == last_elem:
                return insert_pos+1
            insert_pos += 1
        return insert_pos


'''Below is the two pointer method
1. position is pointing to location where the new element can be inserted. 
2. i is running pointer, which keeps running through the list.
3. If the current number and next number is dissimilar then we can send the next number to the
    position pointer where it was pointing.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        position = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[position] = nums[i+1]
                position += 1
            
        return position

        
















sol1 = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol1.removeDuplicates(nums)
for i in range(k):
    print(nums[i])
