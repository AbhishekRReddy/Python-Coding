'''
https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=check-if-an-array-is-sorted
'''


class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        prev = arr[0]
        for i in range(1,n):
            if prev > arr[i]:
                return False
            prev = arr[i]
        return True