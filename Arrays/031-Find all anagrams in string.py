class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        k=len(p)
        n=len(s)

        if k > n:
            return []

        p_freq={}
        window={}

        for ch in p:
            p_freq[ch]=p_freq.get(ch,0)+1
        
        low=0
        high=k
        ans=[]
        while low<high:
            window[s[low]]=window.get(s[low],0)+1
            low+=1

        if window == p_freq:
            ans.append(0)
            

        low=0
        high=k

        while high<n:

            window[s[low]]-=1
            if window[s[low]]==0:
                del window[s[low]]
            low+=1

            window[s[high]]=window.get(s[high],0)+1
            high+=1
            
            if window==p_freq:
                ans.append(low)
        
        return ans

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(s)
        k = len(p)

        if k > n:
            return []

        p_freq = [0] * 256
        window = [0] * 256

        for i in range(k):
            p_freq[ord(p[i])] += 1
            window[ord(s[i])] += 1

        ans = []

        if window == p_freq:
            ans.append(0)

        low = 0
        high = k

        while high < n:

            window[ord(s[low])] -= 1
            low += 1

            window[ord(s[high])] += 1
            high += 1

            if window == p_freq:
                ans.append(low)

        return ans
            

            

        