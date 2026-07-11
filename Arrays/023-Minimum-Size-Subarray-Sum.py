class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        n=len(nums)
        
        res=float('inf')
        s=0
        while high<n:
            s=s+nums[high]

            while s>=target:

                lenth=high-low+1
                res=min(res,lenth)
                s=s-nums[low]
                low+=1
            
            high+=1
        
        if res==float('inf'):
            return 0
        else:
            return res


        