def highest_product(nums):
    nums.sort(reverse = True)
    case1 = nums[0]*nums[1]*nums[2]
    case2 = nums[-1]*nums[-2]*nums[0]   #This is necessary to consider the negative elements if any present.
    return max(case1, case2)
#Above is the brute force method which takes O(nLogn) mainly for the sorting
#But fails when we have the negative numbers

array = [-5,-6,1, 2, 3, 4]
print(highest_product(array)) 