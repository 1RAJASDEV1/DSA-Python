class Solution:
    def getSecondLargest(self, arr):
        lar=-1
        slar=-1
        
        for i in range(len(arr)):
            if arr[i]> lar:
                slar=lar
                lar=arr[i]
            elif slar<arr[i]<lar:
                slar=arr[i]
        return slar            