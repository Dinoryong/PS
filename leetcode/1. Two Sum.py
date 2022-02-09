'''
Brute Force
T.C : O(N2)
S.C : O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


''' 
Two-pass Hash Table
T.C : 
S.C : 

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # {value : index, }
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        print(hashmap)
        # check if hashmap has complement as a key, and simultaneously doesn't have index "i" as a value
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]