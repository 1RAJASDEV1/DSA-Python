class Solution:
    def longestOnes(self, nums: List[int], k: int):

        n = len(nums)

        ans = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                freq[nums[j]] = freq.get(nums[j], 0) + 1

                length = j - i + 1
                diff = length - freq.get(1, 0)

                if diff <= k:
                    ans = max(ans, length)
                else:
                    break

        return ans




class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n=len(nums)

        low=0
        high=0
        ans=0
        freq={}


        while high<n:
            freq[nums[high]]=freq.get(nums[high],0)+1

            lenth=high-low+1
            diff=lenth-freq.get(1,0)

            while diff>k:
                freq[nums[low]]-=1
                if freq[nums[low]]==0:
                    del freq[nums[low]]
                low+=1

                lenth =high-low+1
                diff=lenth-freq.get(1,0)

            ans=max(ans,lenth)
            high+=1
        
        return ans
