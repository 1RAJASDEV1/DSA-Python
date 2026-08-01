class Solution:
    def isHappy(self, n: int) -> bool:

        def find(num):
            sum1 = 0

            while num > 0:
                d = num % 10
                sum1 += d * d
                num //= 10

            return sum1

        slow = n
        fast = n

        while True:

            slow = find(slow)

            fast = find(fast)
            fast = find(fast)

            if slow == fast:
                break

        return slow == 1