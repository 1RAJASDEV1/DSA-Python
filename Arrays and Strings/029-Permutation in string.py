class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k=len(s1)
        n=len(s2)

        if k > n:
            return False

        s1_freq={}

        for ch in s1:
            s1_freq[ch]=s1_freq.get(ch,0)+1
        
        for i in range(n-k+1):

            window={}

            for j in range(i,i+k):
                window[s2[j]]=window.get(s2[j],0)+1

            if window==s1_freq:
                return True
        
        return False

            

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k=len(s1)
        n=len(s2)

        if k > n:
            return False

        s1_freq = {}
        window = {}

        for ch in s1:
            s1_freq[ch]=s1_freq.get(ch,0)+1

        low=0
        high=k

        while low<k:
            window[s2[low]]=window.get(s2[low],0)+1
            low+=1

        if window == s1_freq:
            return True
        
        low=0
        high=k


        while high<n:

            window[s2[low]] -=1
            if window[s2[low]]==0:
                del window[s2[low]]
            low+=1

            window[s2[high]]=window.get(s2[high],0)+1
            high+=1

            if window==s1_freq:
                return True
        
        return False
            


        