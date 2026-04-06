class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0; right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1




        # this works if it only returned the value not the index
        # if target in nums:
        #     return 
        # elif nums[len(nums) // 2] < target:
        #     return self.search(nums[en(nums) // 2: len(nums)], target)
        # elif nums[len(nums) // 2] >= target:
        #     return self.search(nums[0: len(nums) // 2], target)

        return False