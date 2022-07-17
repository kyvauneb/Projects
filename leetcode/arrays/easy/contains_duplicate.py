import random
from typing import List

import timeit


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> tuple([str, bool]):
        # brute force - time: O(n^2), space: O(1) -- this space complexity simply means the algorithm doesn't require extra space to traverse the list

        # loop through each item in the list
        # again loop through all items in the list
        # if x is not y and list[x] === list[y]
        # return True

        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y and nums[x] == nums[y]:
                    return ("Brute Force", True)

        return ["Brute Force", False]


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> tuple([str, bool]):
        # sorting - time: O(nlogn), space: O(1) -- this space complexity simply means the algorithm doesn't require extra space to traverse the list
        # benefit here is that after sorting, duplicates in a list will be adjacent - this allows for easier comparison
        nums.sort()
        for x in range(len(nums)):
            if (x < len(nums)-1) and (nums[x] == nums[x+1]):
                return ("Sort First", True)

        return ("Sort First", False)


class Solution3:
    def containsDuplicate(self, nums: List[int]) -> tuple([str, bool]):
        # hash set - time: O(n), space: O(n) -- since we are creating a new set of worst case, size of the original list
        # benefit: since a set can only contain unique elements, we can add items to a set and if the item already exists within, we can assume there is a dupe
        ## other benefits: Python uses hash tables for dictionaries and sets; are great for insertion, deletion and search
        hashset = set()
        for num in nums:
            if num in hashset:
                return ("Hash Set", True)
            hashset.add(num)

        return ("Hash Set", False)
    
    


positive_list = [1, 32, 24, 61, 18, 88, 20,
                 61, 4, 90, 819, 11, 803, 23, 99, 89, 1]
fail_list_1000 = random.sample(range(10, 1000000), 1000)

method, result = Solution3().containsDuplicate(fail_list_1000)

print("Method: " + method)
print("Result: " + str(result))
print("Time: " + str(timeit.timeit('Solution3().containsDuplicate(fail_list_1000)',
                                   number=100, globals=globals())))
