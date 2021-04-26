"""
python: self 어쩌고 시리즈

그래프도 코테 나오는 유형은
정해져있는 것 같다

"""
class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
