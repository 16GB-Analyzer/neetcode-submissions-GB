class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i in range(len(nums)):
            current=nums[i]
            value = target-current

            if value in seen:
               return [seen[value],i]
            else:
                seen[current]=i




            
        