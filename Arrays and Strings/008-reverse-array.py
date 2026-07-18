class Solution:
    def reverseArray(self, nums):
        
        nums[:]=nums[::-1]
        
        
class Solution:
    def reverseArray(self, nums):
        # code here
        n=len(arr)
        l=0
        r=n-1
        
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        