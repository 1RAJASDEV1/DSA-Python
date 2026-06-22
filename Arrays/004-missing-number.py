class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        
        for i in range(n+1):
            found=False
            for j in range(n):
                if nums[j]==i:
                    found= True
                    break
            if found== False:
                return i

     
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n=len(nums)
#         sum1=n*(n+1)/2
#         sum2=0
#         for i in range(n):
#             sum2=sum2+nums[i]

#         return int(sum1-sum2)

     
        