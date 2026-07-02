class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """             
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        return nums



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        ans=[]

        for i in range(n):
            if nums[i] != 0:
                ans.append(nums[i])
        
        a=len(ans)

        for i in range(a,n):
            ans.append(0)

        nums[:]=ans


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        
        if n==0:return 0

        c=0

        for i in range(n):
            if nums[i] !=0:
                nums[i],nums[c]=nums[c],nums[i]
            
                c=c+1


