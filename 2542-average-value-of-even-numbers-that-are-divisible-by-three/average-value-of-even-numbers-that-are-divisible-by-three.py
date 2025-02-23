class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        for i in nums:
            if i % 6 == 0:  
                a.append(i)
        
        if not a:
            return 0
        
        total_sum = sum(a)
        average = total_sum // len(a)
        return average