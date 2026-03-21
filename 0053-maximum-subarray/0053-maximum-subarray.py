class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=0
        max_sum=nums[0]
        for i in range(len(nums)):
            currentsum+=nums[i]
            if currentsum>max_sum:
                max_sum=currentsum
            if currentsum<0:
                currentsum=0
        return max_sum
