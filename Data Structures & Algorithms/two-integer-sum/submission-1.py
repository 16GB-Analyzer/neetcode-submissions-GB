class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        for i , num in enumerate(nums):
            compliment=n=target-num
            if compliment in seen:
                return [seen[compliment],i]
            seen[num]=i
     