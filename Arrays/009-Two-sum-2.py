class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n=len(numbers)
        i=0
        
        j=1

        for i in range(n):
            x=target-numbers[i]
            j=i+1
            while j<n:
                if x !=numbers[j]:
                    j=j+1
                else:
                    return[i+1,j+1]

            
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]

            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1