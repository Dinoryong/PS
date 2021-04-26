class Solution:
    def singleNumber(self, nums):
        not_duplicate_list = []
        for i in nums:
            if i not in not_duplicate_list:
                not_duplicate_list.append(i)
            else:
                not_duplicate_list.remove(i)
        return not_duplicate_list.pop()