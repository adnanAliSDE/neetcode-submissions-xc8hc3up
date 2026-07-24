class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count={}
        for char in s:
            count=char_count.get(char,0)
            char_count[char]=count+1
        
        for char in t:
            count=char_count.get(char,None)
            if count is None: 
                return False
            
            char_count[char]=count-1
        
        for count in char_count.values():
            if count!=0:
                return False
        
        return True
        