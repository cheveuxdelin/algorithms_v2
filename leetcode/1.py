class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            second_number = target - nums[i]
            if second_number in d:
                return [i, d[second_number]]
            d[nums[i]] = i
        