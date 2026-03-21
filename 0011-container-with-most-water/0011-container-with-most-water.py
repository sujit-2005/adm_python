class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        curr_war=0
        max_war=0
        while left<right:
            curr_war=(right-left)*(min(height[right],height[left]))
            max_war=max(curr_war,max_war)
            if height[right]<height[left]:
                right-=1
            else:
                left+=1
        return max_war
