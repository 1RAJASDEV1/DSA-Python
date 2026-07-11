class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        ans = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):

                if s[j] in seen:
                    break

                seen.add(s[j])
                ans = max(ans, j - i + 1)

        return ans
    
#above is brute force of time complexity O(n^2)  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n=len(s)
        low=0
        high=0
        res=0
        ans=0
        freq={}

        while high<n:

            while s[high] in freq:
                del freq[s[low]]
                low+=1
            
            freq[s[high]]=freq.get(s[high],0)+1
            high+=1
            res=high-low
            ans=max(ans,res)
        
        return ans


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        low = 0
        ans = 0
        freq = {}
        high=0
        while high<n:

            freq[s[high]] = freq.get(s[high], 0) + 1

            length = high - low + 1

            while len(freq) < length:
                freq[s[low]] -= 1

                if freq[s[low]] == 0:
                    del freq[s[low]]

                low += 1
                length = high - low + 1

            ans = max(ans, length)
            high+=1

        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        low = 0
        high = 0
        ans = 0

        last_index = {}

        while high < n:

            if s[high] in last_index and last_index[s[high]] >= low:
                low = last_index[s[high]] + 1

            last_index[s[high]] = high

            length = high - low + 1
            ans = max(ans, length)

            high += 1

        return ans