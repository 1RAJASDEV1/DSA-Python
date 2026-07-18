class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n= len(nums)
        nums.sort()
        i=0
        j=1 
        k=2
        l=n-1

        ans=[]

        for i in range(n-3):

            for j in range(i+1,n-2):
                k=j+1
                l=n-1

                while k<l:
                    s=nums[i]+nums[j]+nums[k]+nums[l]

                    if s==target:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        if temp not in ans:
                            ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                        l=l-1
                    
                    elif s<target:
                        k+=1
                    else:
                        l-=1
        
        return ans
                        
