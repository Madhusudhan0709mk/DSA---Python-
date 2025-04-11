class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq= set()
        for i in nums:
            if i in uniq:
                return True
            else:
                uniq.add(i)
        return False
        