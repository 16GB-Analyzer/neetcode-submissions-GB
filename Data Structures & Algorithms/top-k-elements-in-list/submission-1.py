class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Result=[]
        c=Counter(nums)
        for element,count in c.most_common(k):
            Result.append(element)
        return Result
        

      
      