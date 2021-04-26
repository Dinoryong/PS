```
linked list 에서
특정 node만 제거하는 접근법
1. 삭제할 노드의 값을 next 노드의 값으로 바꾼다
2. 삭제할 노드의 next 노드를 다음 노드의 next 의 값으로 변경 반복
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time and space complexity are both O(1)

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything,
                modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next