class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        n=len(arr)
        k=k%n

        s=list()
        for i in range(n-k,n):
            s.append(arr[i])

        for i in range(n-k):
            s.append(arr[i])    
        
        arr[:]=s



class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        n=len(arr)
        k=k%n

        arr[:]=arr[-k:] + arr[:-k]




