class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1; r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip over all dupes
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    r -= 1; l += 1
                elif sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1

        return res
                    
        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     seen = {}
        #     for j, num in enumerate(nums):
        #         if j == i:
        #             continue
        #         target = -nums[i]
        #         diff = target - num
        #         if diff in seen and seen[diff] != i:
        #             res.append(sorted([nums[i], diff, nums[j]]))
                
        #         seen[num] = j
    
        # res2 = []
        # [res2.append(x) for x in res if x not in res2]

        # return res2
        