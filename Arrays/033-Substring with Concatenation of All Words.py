from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:


        if len(words)==0:
            return []
        check = []

        for p in permutations(words):
            check.append("".join(p))

        n=len(s)

        low=0
        high= len(check[0])

        ans=[]

        while high<=n:

            if s[low:high] in check:
                ans.append(low)

            high+=1
            low+=1
        
        return ans


#above is brute force it wont work because of memory limit

