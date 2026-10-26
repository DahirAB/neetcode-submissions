class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq=defaultdict(int)
        res=[]

        for i in nums:
            feq[i]+=1
        print(feq)
        sortfeq=sorted(feq,key=feq.get,reverse=True)
        for i in range(k):
            res.append(sortfeq[i])
        
        return res


       
        
        