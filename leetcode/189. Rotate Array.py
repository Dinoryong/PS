'''Runtime Error
line => ans[temp[j]] = nums[j]
list assignment index out of range
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        ans = [i for i in range(len(nums))]

        for i in range(len(nums)):
            if (i + k) <= (len(nums) - 1):
                i = i + k
            else:
                i = (i + k) - (len(nums) - 1) - 1
            temp.append(i)

        for j in range(len(temp)):
            ans[temp[j]] = nums[j]
            print(ans)

        for t in range(len(ans)):
            nums[t] = ans[t]

''' time complexity exceeded
Brute Force
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

'''
Using Extra Array 
a의 인덱스 값 항상 크게 가정해보기
Time complexity: O(n). One pass is used to put the numbers in the new array. And another pass to copy the new array to the original one.

Space complexity: O(n). Another array of the same size is used.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a

''' 
Using Cyclic Replacements
Time complexity: O(n). Only one pass is used.
Space complexity: O(1). Constant extra space is used.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1

'''
Using Reverse
Time complexity: O(n). nn elements are reversed a total of three times.

Space complexity: O(1). No extra space is used.
'''
class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)