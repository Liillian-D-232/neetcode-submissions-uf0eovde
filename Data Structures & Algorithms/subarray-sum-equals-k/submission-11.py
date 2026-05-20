class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        sums = {0:1}

        for num in nums:
            curSum += num
            diff = curSum - k

            res += sums.get(diff, 0)
            sums[curSum] = 1 + sums.get(curSum, 0)

            # if diff in sums:
            #     res += 1
            #     curSum = 0
            
            # sums[curSum] = diff
        
        return res