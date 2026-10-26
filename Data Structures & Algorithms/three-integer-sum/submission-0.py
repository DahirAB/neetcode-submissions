class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=(len(nums))
        
        res=set()
        for i in range(n):
            
            l=i+1
            r=n-1
            while l < r:
                threesum =nums[i]+nums[l]+nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    tmp=(nums[i],nums[l],nums[r])
                    res.add(tmp)
                    r-=1
                    l+=1
        return [list(i) for i in res]
        