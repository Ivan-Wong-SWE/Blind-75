class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            even = helper(s, i, i)
            odd = helper(s, i, i + 1)
    
            res = max(res, even, odd, key=len)

        return res

    
def helper(s, i, j):
    while i >= 0 and j <= len(s) - 1 and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]
