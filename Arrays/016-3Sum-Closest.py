class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        min_diff=float('inf')
        res_sum=0
        

        for i in range(n-2):
            j=i+1
            k=n-1
            
            while j<k:
                s=nums[i]+nums[j]+nums[k]
            
                if s==target:
                    res_sum=s
                    return res_sum

                diff=abs(s-target)

                if diff<min_diff:
                    min_diff=diff
                    res_sum=s
                
                if s<target:
                    j+=1
                else :
                    k-=1

        return res_sum
