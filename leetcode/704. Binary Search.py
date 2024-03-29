'''
오름차순 정렬 상태로 주어진다면 binary search를 떠올리자
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                continue
        return -1

'''
simpler
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
	        return nums.index(target)
        else:
	        return -1

''' 
Binary Search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start<=end:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                end = mid - 1
            else:
                start = mid + 1
        return -1