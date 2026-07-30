class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        def isPalindrome(s: str) -> bool:
            l = 0
            r = len(s) - 1
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            return l >= r


        # find 1st possible deletes
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        if l >= r:
            return True

        return isPalindrome(s[l + 1: r + 1]) or isPalindrome(s[l : r])        


        