```
Singly Linked List
1. iteratively 반복으로 풀기
 12345
 21345
 23145

2. recursively 재귀적으로 풀기

```
# Space complexity : O(1)
# Time complexity : O(n)

# Time complexity : O(n)
# Space complexity : O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):  # Iterative
        prev_node, curr_node = None, head
        while curr:
            curr_node.next, prev_node, curr_node = prev_node, curr_node, curr_node.next
        return prev_node

    def reverseList_v1(self, head):  # Recursive
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p