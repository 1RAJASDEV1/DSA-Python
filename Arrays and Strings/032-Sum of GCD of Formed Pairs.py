from math import gcd

class Solution:

    def gcdSum(self, nums: list[int]) -> int:

        
        n=len(nums)
        mx=nums[0]

        prefixgcd=[]

        for i in range(n):

            mx=max(mx,nums[i])

            prefixgcd.append(gcd(mx,nums[i]))

        prefixgcd.sort()

        i=0
        j=len(prefixgcd)-1
        ans=[]
        while i<j:

            ans.append(gcd(prefixgcd[i],prefixgcd[j]))
            i+=1
            j-=1
        
        return sum(ans)

            
    



