class Solution:
    def fun(self,window,t_freq):
        for i in range(256):
            if window[i]<t_freq[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:

        n=len(s)
        m=len(t)
        
        if n<m:
            return ""
        
        window=[0]*256
        t_freq=[0]*256

        for ch in t:
            t_freq[ord(ch)]+=1
        
        low=0
        high=0
        res=float('inf')
        start=-1
        while high<n:

            window[ord(s[high])]+=1

            while self.fun(window,t_freq):

                lenth=high-low+1
                
                if lenth<res:
                    res=lenth
                    start=low
                

                window[ord(s[low])]-=1
                low+=1
            
            high+=1
        
        if res==float('inf'):
            return ""
        else:
            return s[start:start+res]
        
