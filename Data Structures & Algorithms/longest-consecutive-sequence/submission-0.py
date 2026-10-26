class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
       
        maxstreak=0
        curstreak=0
        last=-999999
        for num in nums:
            if num==last:
                continue
            elif num == last+1:
                last=num
                curstreak+=1
                
            else:
                curstreak=1
                last=num
            
            maxstreak=max(maxstreak,curstreak)
        return maxstreak
        