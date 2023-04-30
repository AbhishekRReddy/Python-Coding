class Solution:

    def print2largest(self,arr:list, n):
    # code here
        if n == 1:
            return -1
        first_max = arr[0]
        second_max = float('-inf')
        for i in range(1,len(arr)):
            if arr[i] > first_max:
                second_max = first_max
                first_max = arr[i]
            elif arr[i] > second_max and arr[i] < first_max:
                second_max = arr[i]
        if second_max == float('-inf'):
            return -1
        return second_max  