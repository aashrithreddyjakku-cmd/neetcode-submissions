class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       index={}
       for i,x in enumerate(nums):
            sec = target-x

            if sec in index:
                return [index[sec],i]
            
            index[x]=i
        