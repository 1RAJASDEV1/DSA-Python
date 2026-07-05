class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c1=0
        c2=0
        c3=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                c1+=1
            elif nums[i]==1:
                c2+=1
            else:
                c3+=1
        
        ans=[]

        while c1>0:
            ans.append(0)
            c1-=1
        
        while c2>0:
            ans.append(1)
            c2-=1
        while c3>0:
            ans.append(2)
            c3-=1
        
        nums[:]=ans


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        
        n=len(nums)
        low=0
        mid=0
        high=n-1

        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            
            elif nums[mid]==1:
                
                mid+=1
            
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1

