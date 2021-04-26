"""
sol.1 : sort
0. compare string length
1. string to list
2. reverse one of list
3. compare similarity

sol.2
sort 나
counter 사용하기

sol.3
hash table
"""
# sol.1 스케치
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_list = s.split()
            t_list = t.split()
            if s_list[:-1] == t_list:
                return True
            else:
                return False

# sol.2 스케치
def isAnagram(self, s, t):
       if len(s) != len(t):
           return False
       return sorted(s) == sorted(t)