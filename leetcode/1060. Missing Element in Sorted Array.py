# Runtime Error
'''
IndexError: list index out of range

'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        s = nums[0]
        e = nums[len(nums)-1]
        temp = [i for i in range(s,e+1)]
        for i in range(len(nums)):
            temp.remove(nums[i])
        return temp[k-1]