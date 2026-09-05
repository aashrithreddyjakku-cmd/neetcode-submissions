class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        buck=[[] for i in range(len(nums)+1)]
        for x in nums:
                count[x]=count.get(x,0)+1
        
        for n,c in count.items():
            buck[c].append(n)

        res=[]

        for i in range(len(buck)-1,0,-1):
            for n in buck[i]:
                res.append(n)
                if(len(res)==k):
                    return res
