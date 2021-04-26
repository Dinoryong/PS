```
sol 1. Brute Force 완전탐색
```
# Time complexity : O(n^2)
# Space complexity : O(1)
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

```
sol 2. Hash Map
```
# Time complexity : O(n)
# Space complexity : O(n)

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

```
sol 3. Sorting
```
# Time complexity : O(nlgn)
# Space complexity : O(1) or (O(n))
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

