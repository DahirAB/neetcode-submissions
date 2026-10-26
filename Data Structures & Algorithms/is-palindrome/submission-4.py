class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs="".join(ch.lower() for ch in s if ch.isalnum())
        r=-1
        res=True
        
        for i in cs:
           
            if i == cs[r]:
                res=True
                r=r-1
            else:
                res=False
                break
           
        
        return res
