class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL=0
        l,r=0,0
        char=set()
        while r<len(s):

            if s[r]not in char:
                char.add(s[r])
                length=len(s[l:r+1])
                print(s[l:r+1],length)
                maxL=max(maxL,length)
                r+=1
            else:
                while s[r]in char:
                    char.remove(s[l])
                    l+=1
             
                char.add(s[r])
                r+=1
        return maxL

