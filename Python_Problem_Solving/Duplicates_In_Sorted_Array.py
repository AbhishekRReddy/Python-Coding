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



sol1 = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol1.removeDuplicates(nums)
for i in range(k):
    print(nums[i])