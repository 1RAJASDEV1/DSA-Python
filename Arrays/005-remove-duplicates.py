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