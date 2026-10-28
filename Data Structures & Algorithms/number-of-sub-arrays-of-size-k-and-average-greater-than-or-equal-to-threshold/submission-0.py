class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        T=threshold*k
        res=0
        currsum=0
        L=0 

        for R in range(len(arr)):
            currsum+=arr[R]
            #print(currsum,L,R,res)
            if R-L+1==k:
                if currsum>=T:
                    res+=1
                currsum-=arr[L]
                L+=1
            #print(currsum,L,R,res)
        return res