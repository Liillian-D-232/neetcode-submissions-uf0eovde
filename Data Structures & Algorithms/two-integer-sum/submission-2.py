class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pastMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in pastMap:
                return [pastMap[diff], i]
            pastMap[n] = i