class Solution:
    def segregate0and1(self, arr):
        
        ans=[]
        
        for i in range(len(arr)):
            if arr[i]==1:
                ans.append(1)
            else :
                ans.insert(0,0)
                
        arr[:]=ans[:]    


class Solution:
    def segregate0and1(self, arr):
        
        j=0
        for i in range(len(arr)):
            
            if arr[i]==0:
                arr[i],arr[j]=arr[j],arr[i]
                j=j+1
                
                
        