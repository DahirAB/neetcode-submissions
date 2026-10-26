class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
       currMin,currMax=0,0
       globalMax,globalMin=nums[0],nums[0]
       total=0

       for n in nums:

        currMax=max(currMax+n,n)
        currMin=min(currMin+n,n)
        total+=n
        globalMax=max(globalMax,currMax)
        globalMin=min(globalMin,currMin)
        print (globalMin,globalMax)
       if globalMax > 0:
        return max(total-globalMin,globalMax)
       else:
        return globalMax 
        