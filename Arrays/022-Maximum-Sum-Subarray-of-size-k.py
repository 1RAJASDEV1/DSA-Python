class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        
        window_sum = sum(arr[:k])
        max_sum = window_sum

        i = 0
        j = k

        while j < n:
            window_sum = window_sum - arr[i] + arr[j]
            max_sum = max(max_sum, window_sum)

            i += 1
            j += 1

        return max_sum