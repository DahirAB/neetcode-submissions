class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        minK=r
        while l<=r:
            
            k=(l+r)//2
            t=0
            for pile in piles:
                t+=math.ceil(float(pile)/k)
            if t<=h:
                 minK=k
                 r=k-1
            else:
                l=k+1
            
        return minK