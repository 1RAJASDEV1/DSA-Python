class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        ans = 0

        for i in range(n):

            freq = {}

            for j in range(i, n):

                freq[s[j]] = freq.get(s[j], 0) + 1

                length = j - i + 1
                max_count = max(freq.values())
                diff = length - max_count

                if diff <= k:
                    ans = max(ans, length)
                else:
                    break

        return ans


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        low=0
        high=0
        ans=0
        freq={}


        while high<n:
            freq[s[high]]=freq.get(s[high],0)+1

            lenth=high-low+1
            max_count=max(freq.values())
            diff=lenth-max_count

            while diff>k:
                freq[s[low]]-=1
                
                if freq[s[low]]==0:
                    del freq[s[low]]
                
                low+=1

                lenth=high-low+1
                if len(freq) > 0:
                    max_count = max(freq.values())
                else:
                    max_count = 0
              
                diff=lenth-max_count


            
            ans=max(ans,lenth)
            high+=1
        
        return ans

        