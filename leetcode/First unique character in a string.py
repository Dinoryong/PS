"""
Time complexity : O(N)
since we go through the string of length N two times.
Space complexity : O(1)
because English alphabet contains 26 letters.
"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)

        for idx, char in enumerate(s):
            if cnt[char] == 1:
                return idx
        return -1
