class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in nums:
        #     j = target-i
        #     if (j in nums[1:]):
        #         index_i = nums.index(i)
        #         index_j = nums.index(j)
        #         return [index_i, index_j]
                
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): # Start from the next element
                if nums[i] + nums[j] == target:
                    return [i, j]
            