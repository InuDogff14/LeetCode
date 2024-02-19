class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        count = 0
        for i in range(0,len(s)):
            if(s[i] == s[len(s)-i-1]):
                count = count+1
        
        if(count == len(s)):
            return True
        else:
            return False