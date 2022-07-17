

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
    # brute force
    # create dictionaries of both strings and compare
    # time = O(n), space = O(n)
        
        sDict, tDict = {}, {}
        for letter in s:
            if letter not in sDict:
                sDict.update({letter: 1})
            else:
                sDict.update({letter: sDict.get(letter) + 1})
        
        for letter in t:
            if letter not in tDict:
                tDict.update({letter: 1})
            else:
                tDict.update({letter: tDict.get(letter) + 1})
                
                
        if sDict == tDict:
            return True
        else:
            return False
        

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        # Neetcode solution
        # Same idea as Solution1, a bit less readable
        # time = O(n), space = O(n)
        
        # return Counter(s) == Counter(t) -- this also works
        
        if len(s) != len(t): # always check your inputs
            return False

        countS, countT = {}, {} # create two dictionaries
        
        for i in range(len(s)): # loop through a range of just one of the arrays, as we know they're equal in length
            countS[s[i]] = 1 + countS.get(s[i], 0) # get() means either return the value of the search index, or 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0): # for each key in count s, if the same key in count t is not the same value, return false
                return False
        return True
    
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s) # more memory efficient, less time efficient 


s = "anagram"
t = "nagaram"

print(Solution1().isAnagram(s,t))
