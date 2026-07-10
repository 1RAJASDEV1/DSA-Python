class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        ans = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                freq[fruits[j]] = freq.get(fruits[j], 0) + 1

                if len(freq) <= 2:
                    ans = max(ans, j - i + 1)
                else:
                    break

        return ans
#above is brute force but wont work on leetcode because of time complexity O(n^2)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        freq={}
        n=len(fruits)
        low=0
        high=0

        ans=0
        while high<n:
            freq[fruits[high]]=freq.get(fruits[high],0)+1

            while len(freq)>2:
                freq[fruits[low]]-=1

                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            
            ans = max(ans, high - low + 1)

            high+=1

        return ans
