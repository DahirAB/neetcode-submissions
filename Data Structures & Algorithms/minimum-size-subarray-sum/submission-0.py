class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        currsum=0
        length=float("inf")

        for r in range(len(nums)):
           
            currsum+=nums[r]

            while currsum>=target:
                length=min((r-l)+1,length)
                currsum-=nums[l]
                l+=1
            r+=1

        return 0 if length==float("inf") else length


        