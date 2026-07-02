class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n= len(nums)

        for i in range(n):
            nums[i]=nums[i]*nums[i]

        nums.sort()

        return nums


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n= len(nums)
        a=[]
        b=[]
        for x in range(n):
            if nums[x]<0:
                a.append(nums[x])
            else:
                b.append(nums[x])

        if len(a)==0:
            for x in range(len(b)):
                b[x]=b[x]*b[x]
            return b 

        
        if len(b)==0:
            for x in range(len(a)):
                a[x]=a[x]*a[x]
            a[:]=a[::-1]
            return a  
        
        p1=0
        p2=len(a)-1

        while p1<p2:
            a[p1],a[p2]=a[p2],a[p1]
            p1+=1
            p2-=1

        for c in range(len(a)):
            a[c]=a[c]*a[c]
        
        for d in range(len(b)):
            b[d]=b[d]*b[d]
        
        ans=[]

        i=0
        j=0
        m=len(a)
        n=len(b)
        while i<m and j<n:
            if a[i]<=b[j]:
                ans.append(a[i])
                i+=1
            else:
                ans.append(b[j])
                j+=1
        
        while i<m:
            ans.append(a[i])
            i+=1
        while j<n:
            ans.append(b[j])
            j+=1
        
        
        return ans


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n= len(nums)
        for x in range(n):
            nums[x]=nums[x]*nums[x]
        
        i=0
        j=n-1
        k=n-1
        ans=[0]*n

        while i<=j:
            if nums[i]<nums[j]:
                ans[k]=nums[j]
                j=j-1
                k=k-1
            else:
                ans[k]=nums[i]
                i=i+1
                k=k-1

        return ans
        
        

             