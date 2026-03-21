class Solution:
    def jump(self, nums: List[int]) -> int:
        near =0
        far =0 
        jumps = 0

        while far < len(nums) - 1:
            farest = 0
            for i in range(near, far + 1):
                farest = max(farest, i + nums[i])
            
            near = far + 1
            far = farest
            jumps += 1
        
        return jumps
        