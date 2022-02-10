'''
다시 풀기 2022.02.10

'''
answer = []

for i in nums1:
    if i in nums2:
        idx = nums2.index(i)
        val = nums2.pop(idx)
        answer.append(val)

return answer