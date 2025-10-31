class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)
        total_sum = ((n+1)*(n+2))//2
        arr_sum = sum(arr)
        return total_sum - arr_sum