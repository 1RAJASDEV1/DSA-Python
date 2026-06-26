class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ans=[]
        
        for i in range(len(nums)):
            for j in ans:
                if nums[i] ==j:
                    break
        
            else:
                ans.append(nums[i])

        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n=len(nums)
        i=0 
        j=1

        while j<n:
            if nums[j]==nums[i]:
                j=j+1
            else:
                nums[i+1]=nums[j]
                i=i+1
                j=j+1

        return i+1
