class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        for num in arr:
            if num == K:
                return 1
        return -1