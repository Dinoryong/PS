# Runtime Error
'''
IndexError: list index out of range
    return temp[k-1]

'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        s = nums[0]
        e = nums[len(nums)-1]
        temp = [i for i in range(s,e+1)]
        for i in range(len(nums)):
            temp.remove(nums[i])
        return temp[k-1]

'''
시도.. 
'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        temp = [0]
        for i in range(1, len(nums)):
            temp.append((nums[i] - nums[i - 1] - 1))
        # print(temp)
        while k > 0:
            for i in range(len(temp)):
                if temp[i] == 0:
                    pass
                else:
                    k -= temp[i]

''' 

'''
