class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        prefix=[0]*n
        suffix=[0]*n
        rnums=list(reversed(nums))
        for i in range(n):
            if i == 0:
                prefix[i]=nums[i]
            else:
                prefix[i]=prefix[i-1]*nums[i]
        for i in range(n):
            if i==0:
                suffix[i]=rnums[i]
            else:
                suffix[i]=suffix[i-1]*rnums[i]
        rsuf=list(reversed(suffix))
        for i in range(n):
            if i == 0:
                res[i]=1*(rsuf[i+1] if i+1<n else 1)
            else:
                res[i]=prefix[i-1]*(rsuf[i+1] if i+1<n else 1)
        return res
       

        
       
            

        
            
        
        
        

