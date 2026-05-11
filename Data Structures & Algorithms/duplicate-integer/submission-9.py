"""
input : array [int]
out : bool 

true is appears again, false if not
set?

empty or 1, false

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False        