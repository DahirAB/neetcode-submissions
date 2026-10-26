class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxleft=[0]*n
        maxright=[0]*n
        trapped=0

        for i in range(1,n):

            maxleft[i]=max(maxleft[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i+1])
        
        for i in range(n):
            t=min(maxright[i],maxleft[i])-height[i]
            if t<1:
                t=0
            trapped+=t

        
        return trapped

        