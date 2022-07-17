from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # idea: create a dictionary of numbers in the list and a list of each numbers index
        # if there are two keys in the dictionary equal to the target, get the first two items of their corresponding lists in the dict
        
        if len(nums) < 2:
            return []
        
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]
        
        hashset = {}
        for i in range(len(nums)):
            # if nums[i] not in hashset:
                hashset.update({nums[i]: i})
            
        for i in range(len(nums)):
            if target - nums[i] in hashset and hashset.get(target - nums[i]) != i:
                return [i, hashset.get(target - nums[i])]

        return []
            
                
#nums = [-1, -2, -3, -4, -5]
#target = -8
nums = [3, 2, 4]
target = 6

print(Solution().twoSum(nums, target))
