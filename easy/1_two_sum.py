# use a dictionary as it { key: value } pairs, where the key provides access to the value in O(n) time.

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if (target - num) in seen:
                return [seen[diff], i]

            seen[num] = i
        
        return []