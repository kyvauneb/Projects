from cgi import test
from typing import List

# prequisite: array must be sorted

def binarySearch(arr: List[int], target: int): # move the middle of the search field to the halfway mark of each valid search zone (achieved by halving the input array on each pass)
    l = 0
    r = len(arr) - 1 # we want the index; arrays are zero-indexed
    
    while (l <= r): # l should always move closer to r
        m = (l + r) // 2
        if (target > arr[m]):
            l = m + 1
        elif (target < arr[m]):
            r = m - 1
        else:
            return m
    
    return -1
        

test_array = [1, 4, 8, 32, 44, 58, 81, 99]

print(str(binarySearch(test_array, 81)))