class Solution:
    def reverseArray(self, nums):
        
        nums[:]=nums[::-1]
        
class Solution:
    def reverseArray(self, nums):
        
        n=len(nums)
        i=0
        j=n-1
        
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1