class Solution:
    def isPalindrome1(self, s: str) -> bool: # faster than 81% of submissions
        s = ''.join(filter(str.isalnum, s)).lower()
        
        if s == s[::-1]:
            return True

        return False
    
    def isPalindrome2(self, s:str) -> bool: # faster than 50% of submissions
        s = ''.join(filter(str.isalnum, s)).lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


s = "A man, a plan, a canal: Panafma"

print(str(Solution().isPalindrome2(s)))
