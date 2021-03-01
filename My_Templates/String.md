# String

---------

> [toc]





## reverse

> leetcode : Reverse Srting, 



```python
# 라이브러리 사용
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
```



```python
# 
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
```



```python
# 투 포인터같이
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
```

