"""
python: Counter, enumerate 복습
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int] -> Lis[int]):
        result = []
        cnt = dict(Counter(nums1))

        for num in nums2:
            if num in cnt and cnt[num] != 0:
                result.append(num)
                cnt[num] = cnt[num] - 1
        return result