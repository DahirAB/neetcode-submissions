class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "====="
        else:
            return "GGPDSA".join(strs)
            
            

    def decode(self, s: str) -> List[str]:
        if s =="=====":
            return []
        return s.split("GGPDSA")
        
        

