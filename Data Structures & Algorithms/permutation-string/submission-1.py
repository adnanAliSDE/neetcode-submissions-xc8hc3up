class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        cs1={}
        for char in s1:
            cs1[char]=cs1.get(char,0)+1
        
        left,right=0,len(s1)-1
        cs2={}

        for char in s2[left:right+1]:
            cs2[char]=cs2.get(char,0)+1

        if cs2==cs1:
            return True

        while right<len(s2)-1:
            left_count=cs2[s2[left]]
            if left_count==1:
                cs2.pop(s2[left])
            else:
                cs2[s2[left]]=left_count-1

            left+=1
            right+=1
            right_count=cs2.get(s2[right],0)+1
            cs2[s2[right]]=right_count
            if cs1==cs2:
                return True
        return False