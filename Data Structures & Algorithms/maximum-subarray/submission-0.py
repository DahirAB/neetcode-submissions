class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currs=0

        for n in nums:
            currs=max(currs,0)
            currs+=n
            maxsum=max(maxsum,currs)
        
        return maxsum