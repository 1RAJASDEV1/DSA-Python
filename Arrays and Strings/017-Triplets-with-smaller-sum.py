class Solution:
    def countTriplets(self, sum, arr):
        n=len(arr)
        arr.sort()
        count=0
        for i in range(n-2):
            
            for j in range(i+1,n):
                
                for k in range(j+1,n):
                    s=arr[i]+arr[j]+arr[k]
                
                    if s<sum:
                        count+=1
                        k=k-1
                    else:
                        j=j+1
                        continue
        return count

#above solution is just for understanding its brute force and time limit is exceeded.

class Solution:
    def countTriplets(self, sum, arr):
        n=len(arr)
        arr.sort()
        count=0
        for i in range(n-2):
            j=i+1
            k=n-1
            
            
            while j<k:
                s=arr[i]+arr[j]+arr[k]
                
                if s<sum:
                    
                    count=count+k-j
                    j+=1
                    
                else:
                    k-=1
                    continue
        return count