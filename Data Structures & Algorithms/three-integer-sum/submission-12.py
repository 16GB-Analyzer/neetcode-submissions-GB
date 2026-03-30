class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Essential for the two-pointer approach

        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization: smallest number > 0 means no zero-sum possible
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1  # Move right pointer to decrease the sum
                elif three_sum < 0:
                    l += 1  # Move left pointer to increase the sum
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # Skip duplicates for the second element
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res  # You must return the final list