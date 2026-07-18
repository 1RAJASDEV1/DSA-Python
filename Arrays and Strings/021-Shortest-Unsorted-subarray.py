class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = nums[:]
        temp.sort()

        n = len(nums)
        left = 0
        right = n - 1

        while left < n and nums[left] == temp[left]:
            left += 1

        while right >= 0 and nums[right] == temp[right]:
            right -= 1

        if left > right:
            return 0

        return right - left + 1

