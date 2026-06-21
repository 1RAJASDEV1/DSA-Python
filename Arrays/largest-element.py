class Solution:
    def largest(self, arr):
        
        max = arr[0]
        for i in range(len(arr)):
            if arr[i]>max:
                max=arr[i]
            
            
        return max
        
