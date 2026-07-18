class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)

        freq = {}
        low = 0
        high = 0
        res = -1

        while high < n:
            freq[s[high]] = freq.get(s[high], 0) + 1

            while len(freq) > k:
                freq[s[low]] -= 1

                if freq[s[low]] == 0:
                    del freq[s[low]]

                low += 1

            if len(freq) == k:
                res = max(res, high - low + 1)

            high += 1

        return res